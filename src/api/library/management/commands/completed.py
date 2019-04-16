from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from library.models import Workshop


class Command(BaseCommand):
    help = 'Get number of users that completed more than -min- percentage'

    def add_arguments(self, parser):
        parser.add_argument('data', nargs='+', type=int)

    def handle(self, *args, **options):
        try:
            min = options['data'][0]
        except IndexError:
            raise CommandError('please put minimum percentage')
        users = User.objects.all()
        workshops = Workshop.objects.all()

        for workshop in workshops:
            result = 0
            print(workshop)

            for user in users:
                user_data = Workshop.objects.with_shown_percentage(user=user).get(pk=workshop.id)
                if user_data.shown_percentage > min:
                    result += 1

            print(result)
