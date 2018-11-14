from coretabs.admin import site
from django.contrib.admin import ModelAdmin, TabularInline
from .models import Profile, SocialLink, Team


class SocialLinkInline(TabularInline):
    model = SocialLink
    extra = 1


class ProfileAdmin(ModelAdmin):
    inlines = (SocialLinkInline,)


site.register(Profile, ProfileAdmin)
site.register(SocialLink)
site.register(Team)
