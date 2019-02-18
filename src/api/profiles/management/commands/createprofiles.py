from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction

from ...models import Profile
User = get_user_model()


class Command(BaseCommand):
    help = 'Create profiles for users.'

    def handle(self, *args, **options):
        users = User.objects.all()

        with transaction.atomic():
            for user in users:
                if Profile.objects.filter(user=user).exists():
                    self.stdout.write(f'Ignored {user.username}')
                    continue

                Profile.objects.create(user=user)
                self.stdout.write(f'Added {user.username}')

        self.stdout.write(self.style.SUCCESS(f'Finished successfully'))
