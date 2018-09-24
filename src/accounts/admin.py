from coretabs.admin import site
from rest_framework.authtoken.admin import Token, TokenAdmin
from allauth.account.admin import EmailAddress, EmailAddressAdmin
from django.contrib.auth.admin import Group, GroupAdmin, User, UserAdmin
from django.contrib.sites.admin import Site, SiteAdmin
from .models import Batch


site.register(Token, TokenAdmin)
site.register(EmailAddress, EmailAddressAdmin)
site.register(User, UserAdmin)
site.register(Group, GroupAdmin)
site.register(Site, SiteAdmin)
site.register(Batch)
