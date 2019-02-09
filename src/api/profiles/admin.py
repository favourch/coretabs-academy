from coretabs.admin import site
from django.contrib.admin import ModelAdmin, TabularInline
from .models import Profile, SocialLink, Team, Certificate, CertificateTemplate, CertificateSignature


class SocialLinkInline(TabularInline):
    model = SocialLink
    extra = 1


class ProfileAdmin(ModelAdmin):
    inlines = (SocialLinkInline,)


site.register(Profile, ProfileAdmin)
site.register(SocialLink)
site.register(Team)
site.register(Certificate)
site.register(CertificateTemplate)
site.register(CertificateSignature)
