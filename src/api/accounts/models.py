import requests

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from django.db import models
from django.db.models.signals import post_delete
from django.db import transaction

from django.dispatch import receiver

from rest_framework.renderers import JSONRenderer

from accounts.serializers import MailingListSerializer

from coretabs import settings

User = get_user_model()


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
        emails_per_call = 2
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
