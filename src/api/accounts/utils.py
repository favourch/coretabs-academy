import requests

from django.conf import settings

from django.core import mail
from django.template.loader import render_to_string

from .helper_serializers import MailingListSerializer


def send_password_reset_mail(user, token, uid):
    password_reset_url = f'{settings.SPA_BASE_URL}/reset-password/{uid}/{token}'
    ctx = {
        'password_reset_url': password_reset_url,
    }
    email_template = 'accounts/email/password_reset_key'
    msg = render_mail(email_template, user.email, ctx)
    msg.send()


def send_confirmation_mail(user, email, primary, token, uid):
    activate_url = f'{settings.SPA_BASE_URL}/confirm-account/{uid}/{token}'
    ctx = {
        'user': user.username,
        'activate_url': activate_url,
    }

    if primary:
        email_template = 'accounts/email/email_confirmation'
    else:
        email_template = 'accounts/email/new_email_confirmation'

    msg = render_mail(email_template, email, ctx)
    msg.send()


def send_email_changed_mail(user, new_email):
    ctx = {
        'user': user.username,
        'new_email': new_email,
    }
    email_template = 'accounts/email/email_changed'
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


def update_email_in_mailing_lists(user, old_email):
    json_member = MailingListSerializer(user).data

    for gr in user.groups.filter(name__startswith='batch'):
        mailing_list = f'{gr.name}@{settings.MAILGUN_LIST_DOMAIN}'
        requests.put(f'https://api.mailgun.net/v3/lists/{mailing_list}/members/{old_email}',
                     auth=('api', settings.MAILGUN_API_KEY),
                     data=json_member)
