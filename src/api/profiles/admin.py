from django.conf import settings

from coretabs.admin import site, MyActionForm

from django.contrib.admin import ModelAdmin
from .models import Profile, Certificate, CertificateTemplate, CertificateSignature

from .utils import render_mail


class ProfileAdmin(ModelAdmin):
    action_form = MyActionForm
    actions = ['generate_and_send_certificates']
    search_fields = ('user__username', 'user__first_name', 'user__email')
    ordering = ('user__date_joined', 'user__first_name',)

    def _send_certificate_email(self, certificate, email):
        context = {'certificate_url': f'{settings.SPA_BASE_URL}/certificates/{certificate.id}', }

        msg = render_mail(
            'profiles/email/certificate',
            email,
            context)
        msg.send()

    def generate_and_send_certificates(self, request, queryset):
        template_heading = request.POST['x']
        template = CertificateTemplate.objects.get(heading=template_heading)

        for profile in queryset:
            # TODO: see if profile has already this certificate
            certificate = Certificate(profile=profile, full_name=profile.user.first_name, template=template)
            certificate.save()
            self._send_certificate_email(certificate, profile.user.email)


site.register(Profile, ProfileAdmin)
site.register(Certificate)
site.register(CertificateTemplate)
site.register(CertificateSignature)
