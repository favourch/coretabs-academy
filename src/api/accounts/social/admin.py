from django.contrib.admin import ModelAdmin
from coretabs.admin import site

from .models import UserSocialAuth


class UserSocialAuthAdmin(ModelAdmin):
    list_display = ('user', 'provider', 'uid')
    list_filter = ('provider',)


site.register(UserSocialAuth, UserSocialAuthAdmin)
