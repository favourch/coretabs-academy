import requests
from .helper_serializers import MailingListSerializer

from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.auth.admin import Group, GroupAdmin, User, UserAdmin
from django.contrib.sites.admin import Site, SiteAdmin

from rest_framework.authtoken.admin import Token, TokenAdmin

from coretabs.admin import site, MyActionForm
from coretabs import settings

from .models import Batch, EmailAddress, Account
from .utils import render_mail
from .actions import send_email, SendUserEmails


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
    actions = ['add_or_change_batch', 'add_or_change_batch_and_send_email', 'remove_batch',
               'send_complete_content_email', send_email]
    list_display = ('username', 'email', 'first_name', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', HasBatchFilter)
    ordering = ('date_joined', 'username')

    def get_urls(self):
        from django.urls import path

        urls = super().get_urls()
        my_urls = [
            path('action/send_email', SendUserEmails.as_view(), name='send_email')
        ]

        return my_urls + urls

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

    def add_or_change_batch_and_send_email(self, request, queryset):
        group_name = request.POST['x']
        group = Group.objects.filter(name=group_name).first()

        for user in queryset:
            for gr in user.groups.filter(name__startswith='batch'):
                user.groups.remove(gr)
                self._remove_user_from_mailing_list(user, gr.name)

            context = {'start_date': group.batch_details.start_date,
                       'user': user.first_name}
            user.groups.add(group)
            self._add_user_into_mailing_list(user, group.name)
            msg = render_mail(
                'accounts/email/starting_batch_details_action',
                user.email,
                context)
            msg.send()

    def remove_batch(self, request, queryset):
        for user in queryset:
            for gr in user.groups.filter(name__startswith='batch'):
                user.groups.remove(gr)
                self._remove_user_from_mailing_list(user, gr.name)

    def _calcute_percentage(self, user, track):
        percentage = 0
        workshops = track.workshops.with_shown_percentage(user=user).filter(tracks=track)

        for workshop in workshops:
            percentage += workshop.shown_percentage

        return percentage / workshops.count()

    def send_complete_content_email(self, request, queryset):
        tracks = {
            'Backend': ('ياسر', 'الباكند'),
            'Frontend': ('محمد', 'الفرونت')
        }

        for user in queryset:

            track = user.account.track

            template_name = 'accounts/email/start_content_action'
            context = {
                'user': user.first_name,
                'track_author': tracks['Backend'][0]
            }

            if track is not None and track.title in tracks.keys():
                percentage = self._calcute_percentage(user, track)

                if percentage > 0:

                    if percentage == 100:
                        continue

                    if percentage < 25:
                        percentage = 25

                    template_name = 'accounts/email/complete_content_action'

                    context = {'percentage': int(percentage),
                               'track_author': tracks[track.title][0],
                               'track_name': tracks[track.title][1],
                               'user': user.first_name}

            msg = render_mail(template_name, user.email, context)
            msg.send()


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

            msg = render_mail(
                'accounts/email/starting_batch_details',
                f'{batch.group.name}@{settings.MAILGUN_LIST_DOMAIN}',
                context)
            msg.send()

    def send_approval_emails(self, request, queryset):
        for batch in queryset:
            context = {'start_date': batch.start_date, }

            msg = render_mail(
                'accounts/email/approve_user',
                f'{batch.group.name}@{settings.MAILGUN_LIST_DOMAIN}',
                context)
            msg.send()


class AccountAdmin(ModelAdmin):
    search_fields = ('user__username', 'user__first_name', 'user__email')
    ordering = ('user__date_joined', 'user__first_name',)


class EmailAddressAdmin(ModelAdmin):
    search_fields = ('email', 'user__username', 'user__first_name',)
    ordering = ('user__date_joined', 'email',)


site.register(Token, TokenAdmin)
site.register(EmailAddress, EmailAddressAdmin)
site.register(User, MyUserAdmin)
site.register(Group, GroupAdmin)
site.register(Site, SiteAdmin)
site.register(Batch, BatchAdmin)
site.register(Account, AccountAdmin)
