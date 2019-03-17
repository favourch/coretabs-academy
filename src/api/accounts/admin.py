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
    list_display = ('username', 'email', 'first_name', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', HasBatchFilter)
    ordering = ('date_joined', 'username')

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
    search_fields = ('user__username', 'user__first_name',)


site.register(Token, TokenAdmin)
site.register(EmailAddress)
site.register(User, MyUserAdmin)
site.register(Group, GroupAdmin)
site.register(Site, SiteAdmin)
site.register(Batch, BatchAdmin)
site.register(Account, AccountAdmin)
