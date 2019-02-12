from django.core import mail
from django.template.loader import render_to_string


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
