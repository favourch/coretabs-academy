from coretabs.admin import site
from rest_framework.authtoken.admin import Token, TokenAdmin
from allauth.account.admin import EmailAddress, EmailAddressAdmin
from django.contrib.auth.admin import Group, GroupAdmin, UserAdmin
from .models import User
from django.contrib.sites.admin import Site, SiteAdmin


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'is_approved', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


site.register(Token, TokenAdmin)
site.register(EmailAddress, EmailAddressAdmin)
site.register(User, CustomUserAdmin)
site.register(Group, GroupAdmin)
site.register(Site, SiteAdmin)
