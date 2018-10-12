from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import Group, GroupAdmin, User, UserAdmin
from django.contrib.sites.admin import Site, SiteAdmin

from django.core import mail
from django.template.loader import render_to_string

from rest_framework.authtoken.admin import Token, TokenAdmin
from allauth.account.admin import EmailAddress, EmailAddressAdmin

from coretabs.admin import site
from coretabs import settings

from .models import Batch


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
site.register(User, UserAdmin)
site.register(Group, GroupAdmin)
site.register(Site, SiteAdmin)
site.register(Batch, BatchAdmin)

