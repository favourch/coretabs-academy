from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import transaction

User = get_user_model()


class Command(BaseCommand):
    help = 'Adds number of users to a specified batch.'

    def add_arguments(self, parser):
        parser.add_argument('limit', type=int)
        parser.add_argument('batch', type=str)

    def handle(self, *args, **options):
        limit = options['limit']
        batch = options['batch']

        batch = Group.objects.filter(name=batch).first()
        if not batch:
            raise CommandError('Batch name does not exist.')

        users = User.objects.all().order_by('date_joined')

        print('Ready to start.')
        with transaction.atomic():
            for user in users:
                if limit < 1:
                    break
                if user.groups.all():
                    continue

                user.groups.add(batch)
                print(f'Added {user.username}')
                limit -= 1

        self.stdout.write(self.style.SUCCESS(f'Successfully added {options["limit"] - limit} users'))
