import requests
from .serializers import MailingListSerializer
from rest_framework.renderers import JSONRenderer

from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.auth.admin import Group, GroupAdmin, User, UserAdmin
from django.contrib.sites.admin import Site, SiteAdmin

from django.core import mail
from django.template.loader import render_to_string

from rest_framework.authtoken.admin import Token, TokenAdmin
from allauth.account.admin import EmailAddress, EmailAddressAdmin

from coretabs.admin import site, MyActionForm
from coretabs import settings

from .models import Batch


class HasBatchFilter(SimpleListFilter):
    title = 'Batch'

    parameter_name = 'groups'

    def lookups(self, request, model_admin):

        return (
            ('t', 'has batch'),
            ('f', 'has no batch'),
        )

    def queryset(self, request, queryset):
        if self.value() == 't':
            return queryset.filter(groups__name__startswith='batch')
        if self.value() == 'f':
            return queryset.exclude(groups__name__startswith='batch')


class MyUserAdmin(UserAdmin):
    action_form = MyActionForm
    actions = ['add_or_change_batch', 'remove_batch', ]
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', HasBatchFilter)

    def _add_user_into_mailing_list(self, user, mailing_list_name):
        json_member = MailingListSerializer(user).data
        mailing_list = f'{mailing_list_name}@{settings.MAILGUN_LIST_DOMAIN}'

        requests.post(f'https://api.mailgun.net/v3/lists/{mailing_list}/members',
                      auth=('api', settings.MAILGUN_API_KEY),
                      data=json_member)

    def _remove_user_from_mailing_list(self, user, mailing_list_name):
        mailing_list = f'{mailing_list_name}@{settings.MAILGUN_LIST_DOMAIN}'

        requests.delete(f'https://api.mailgun.net/v3/lists/{mailing_list}/members/{user.email}',
                        auth=('api', settings.MAILGUN_API_KEY))

    def add_or_change_batch(self, request, queryset):
        group_name = request.POST['x']
        group = Group.objects.filter(name=group_name).first()

        for user in queryset:
            for gr in user.groups.filter(name__startswith='batch'):
                user.groups.remove(gr)
                self._remove_user_from_mailing_list(user, gr.name)

            user.groups.add(group)
            self._add_user_into_mailing_list(user, group.name)

    def remove_batch(self, request, queryset):
        for user in queryset:
            for gr in user.groups.filter(name__startswith='batch'):
                user.groups.remove(gr)
                self._remove_user_from_mailing_list(user, gr.name)


class BatchAdmin(ModelAdmin):
    actions = ['send_approval_emails', 'send_starting_batch_details']
    readonly_fields = ('users', )

    def users(self, obj):
        result = ''
        for user in obj.group.user_set.all():
            result += f'{user.username} ({user.first_name}) - '
        return result

    users.short_description = 'Users'

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def send_starting_batch_details(self, request, queryset):
        for batch in queryset:
            context = {'start_date': batch.start_date, }

            msg = self.render_mail(
                        'account/email/starting_batch_details',
                        f'{batch.group.name}@{settings.MAILGUN_LIST_DOMAIN}',
                        context)
            msg.send()

    def send_approval_emails(self, request, queryset):
        for batch in queryset:
            context = {'start_date': batch.start_date, }

            msg = self.render_mail(
                        'account/email/approve_user',
                        f'{batch.group.name}@{settings.MAILGUN_LIST_DOMAIN}',
                        context)
            msg.send()

    def render_mail(self, template_prefix, email, context):
        subject = render_to_string('{0}_subject.txt'.format(template_prefix),
                                   context)
        # remove superfluous line breaks
        subject = " ".join(subject.splitlines()).strip()

        template_name = '{0}_message.{1}'.format(template_prefix, 'html')
        body = render_to_string(template_name,
                                context).strip()

        msg = mail.EmailMessage(subject=subject,
                                body=body,
                                to=[email])
        msg.content_subtype = 'html'
        return msg


site.register(Token, TokenAdmin)
site.register(EmailAddress, EmailAddressAdmin)
site.register(User, MyUserAdmin)
site.register(Group, GroupAdmin)
site.register(Site, SiteAdmin)
site.register(Batch, BatchAdmin)

