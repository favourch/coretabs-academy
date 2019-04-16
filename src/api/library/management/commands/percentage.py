from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from library.models import Workshop


class Command(BaseCommand):
    help = 'Get users shown percentage'

    def handle(self, *args, **options):
        users = User.objects.all()
        users_count = users.count()
        workshops = Workshop.objects.all()

        for workshop in workshops:
            result = 0
            print(workshop)

            for user in users:
                user_data = Workshop.objects.with_shown_percentage(user=user).get(pk=workshop.id)
                result += int(user_data.shown_percentage)

            print(result / users_count)
