from django.conf import settings

from django.core import mail
from django.template.loader import render_to_string


def create_token(token_model, user):
    token, created = token_model.objects.get_or_create(user=user)
    return token


def create_user(cd):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    user = User.objects.create_user(cd['username'], cd['email'], cd['password1'], first_name=cd['first_name'])
    return user


def setup_user_email(user):
    from .models import EmailAddress

    assert not EmailAddress.objects.filter(user=user).exists()
    email = EmailAddress.objects.create(user=user, email=user.email, primary=True, verified=False)
    return email


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
