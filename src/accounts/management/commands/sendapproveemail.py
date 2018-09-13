from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from allauth.account.utils import user_pk_to_url_str
from accounts.tokens import approve_user_token_generator
from django.core import mail
from django.template.loader import render_to_string

User = get_user_model()


class Command(BaseCommand):
    help = 'Sends approvement emails to a batch users.'

    def add_arguments(self, parser):
        parser.add_argument('batch', type=str)

    def handle(self, *args, **options):
        batch = options['batch']
        users = User.objects.filter(groups__name=batch)

        if not users:
            raise CommandError('No users to email or bad batch name.')

        with mail.get_connection(backend='django.core.mail.backends.smtp.EmailBackend') as connection:

            for user in users:
                uid = user_pk_to_url_str(user)
                key = approve_user_token_generator.make_token(user)
                email = user.email

                url = f'https://coretabs.net/approve-user/{uid}/{key}'
                context = {'user': user,
                           'url': url}

                msg = self.render_mail(
                    'account/email/approve_user',
                    email,
                    context,
                    connection)

                msg.send()
                print(f'{user.username} emailed')

        self.stdout.write(self.style.SUCCESS(f'Successfully sent {len(users)} emails'))

    def render_mail(self, template_prefix, email, context, connection):
        subject = render_to_string('{0}_subject.txt'.format(template_prefix),
                                   context)
        # remove superfluous line breaks
        subject = " ".join(subject.splitlines()).strip()

        template_name = '{0}_message.{1}'.format(template_prefix, 'html')
        body = render_to_string(template_name,
                                context).strip()

        msg = mail.EmailMessage(subject=subject,
                                body=body,
                                to=[email],
                                connection=connection)
        msg.content_subtype = 'html'
        return msg
