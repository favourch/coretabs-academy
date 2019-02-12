from django.conf import settings

from django.core import mail
from django.template.loader import render_to_string


def send_password_reset_mail(user, token, uid):
    password_reset_url = f'{settings.SPA_BASE_URL}/reset-password/{uid}/{token}'
    ctx = {
        'password_reset_url': password_reset_url,
    }
    email_template = 'accounts/email/password_reset_key'
    msg = render_mail(email_template, user.email, ctx)
    msg.send()


def send_confirmation_mail(user, token, uid):
    activate_url = f'{settings.SPA_BASE_URL}/confirm-account/{uid}/{token}'
    ctx = {
        'user': user.username,
        'activate_url': activate_url,
    }
    email_template = 'accounts/email/email_confirmation'
    msg = render_mail(email_template, user.email, ctx)
    msg.send()


def render_mail(template_prefix, email, context):
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
