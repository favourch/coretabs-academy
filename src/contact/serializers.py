from rest_framework import serializers
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    email = serializers.EmailField(required=True)

    body = serializers.CharField(required=True)

    def render_mail(self, template_prefix, emails, context):
        subject = render_to_string(
            '{0}_subject.txt'.format(template_prefix), context)
        subject = ''.join(subject.splitlines()).strip()
        from_email = settings.DEFAULT_FROM_EMAIL
        template_name = '{0}_message.html'.format(template_prefix)
        body = render_to_string(template_name, context)
        msg = EmailMessage(subject, body, from_email, emails)
        msg.content_subtype = 'html'
        msg.send(fail_silently=False)

    def save(self):
        ctx = {
            'name': self.validated_data['name'],
            'email': self.validated_data['email'],
            'body': self.validated_data['body'],
        }
        to_emails = settings.MANAGERS_EMAILS + [self.validated_data['email']]
        self.render_mail('contact/email/contact_email', to_emails, ctx)
