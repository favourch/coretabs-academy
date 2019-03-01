import requests

from django.conf import settings

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from django.db import models
from django.db.models.signals import post_save, post_delete
from django.db import transaction

from django.dispatch import receiver
from .signals import user_updated

from rest_framework.renderers import JSONRenderer

from .managers import EmailAddressManager
from .tokens import confirm_email_token_generator
from .utils import send_confirmation_mail, update_email_in_mailing_lists
from .helper_serializers import MailingListSerializer
from django.utils.http import int_to_base36

from library.models import Track, BaseLesson

User = get_user_model()


class EmailAddress(models.Model):

    user = models.ForeignKey(User,
                             verbose_name=_('user'),
                             related_name='email_addresses',
                             on_delete=models.CASCADE)
    email = models.EmailField(unique=True,
                              max_length=128,
                              verbose_name=_('e-mail address'))
    verified = models.BooleanField(verbose_name=_('verified'), default=False)
    primary = models.BooleanField(verbose_name=_('primary'), default=False)

    objects = EmailAddressManager()

    class Meta:
        verbose_name = _("email address")
        verbose_name_plural = _("email addresses")

    def __str__(self):
        return "%s (%s)" % (self.email, self.user)

    def set_as_primary(self):
        old_primary = EmailAddress.objects.get_primary(self.user)
        if old_primary:
            old_email = old_primary.email
            old_primary.delete()

        self.primary = True
        self.save()
        self.user.email = self.email
        self.user.save()

        update_email_in_mailing_lists(self.user, old_email)
        user_updated.send(sender=User, user=self.user)

    def send_confirmation(self):
        if not self.verified:
            token = confirm_email_token_generator.make_token(self)
            uid = int_to_base36(self.pk)

            send_confirmation_mail(self.user, self.email, self.primary, token, uid)

    def confirm(self):
        is_changed = False

        self.verified = True

        if not self.primary:
            self.set_as_primary()
            is_changed = True

        self.save()
        return is_changed


class Account(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.SET_NULL,
                              verbose_name=_('track'), null=True)
    last_opened_lesson = models.ForeignKey(BaseLesson,
                                           on_delete=models.SET_NULL,
                                           verbose_name=_('last opened lesson'), null=True)

    def __str__(self):
        return f'{self.user.first_name} ({self.user.username})'

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')


@receiver(post_save, sender=User)
def create_user_account_email_token(sender, instance, created, **kwargs):
    if created:
        EmailAddress.objects.create(user=instance, email=instance.email, primary=True, verified=False)
        Account.objects.create(user=instance)
        Token.objects.create(user=instance)


class Batch(models.Model):
    group = models.OneToOneField(Group, related_name='batch_details',
                                 null=True, blank=True, on_delete=models.CASCADE,
                                 verbose_name='group (Added Automatically)')
    name = models.CharField(max_length=20)
    users_number = models.PositiveIntegerField(verbose_name='users number')
    start_date = models.DateField()

    class Meta:
        permissions = (
            ('access_workshops', 'Allow User to see Workshops'),
        )
        verbose_name = 'batch'
        verbose_name_plural = 'batches'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.group:
            group = Group.objects.create(name=self.name)
            self.group = group

        self.prepare_batch()
        self.prepare_mailing_list()
        super().save()

    def _create_mailing_list(self, mailing_list):
        requests.post(f'https://api.mailgun.net/v3/lists',
                        auth=('api', settings.MAILGUN_API_KEY),
                        data={'address': mailing_list})

    def _add_group_into_mailing_list(self, group_name, mailing_list):
        offset = 0
        emails_per_call = 900
        group_users = User.objects.filter(groups__name=group_name)

        current_members = group_users.values('email', 'first_name')[offset:offset + emails_per_call]
        while current_members:
            json_members = JSONRenderer().render(MailingListSerializer(current_members, many=True).data)

            requests.post(f'https://api.mailgun.net/v3/lists/{mailing_list}/members.json',
                        auth=('api', settings.MAILGUN_API_KEY),
                        data={'members': json_members})

            offset += emails_per_call
            current_members = group_users.values('email', 'first_name')[offset:offset + emails_per_call]

    def prepare_mailing_list(self):
        group_name = self.group.name
        mailing_list = f'{group_name}@{settings.MAILGUN_LIST_DOMAIN}'
        
        self._create_mailing_list(mailing_list)
        self._add_group_into_mailing_list(group_name, mailing_list)

    def prepare_batch(self):
        batch_group = self.group
        users = User.objects.all().order_by('date_joined')
        limit = self.users_number

        with transaction.atomic():
            for user in users:
                if limit < 1:
                    break
                if user.groups.all():
                    continue

                user.groups.add(batch_group)
                limit -= 1

        final_users_number = self.users_number - limit
        self.users_number = final_users_number

    def __str__(self):
        return self.name


@receiver(post_delete, sender=Batch, dispatch_uid = 'delete_batch')
def delete_batch_group_with_mailing_list(sender, instance, **kwargs):
    requests.delete(f'https://api.mailgun.net/v3/lists/{instance.group.name}@{settings.MAILGUN_LIST_DOMAIN}',
                        auth=('api', settings.MAILGUN_API_KEY))

    instance.group.delete()
