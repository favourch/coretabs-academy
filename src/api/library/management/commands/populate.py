from django.core.management.base import BaseCommand, CommandError
from ._populator import create_track, create_users


class Command(BaseCommand):
    help = 'Creates dummy data for performance tests'

    def add_arguments(self, parser):
        parser.add_argument('data', nargs='+', type=int)

    def handle(self, *args, **options):
        try:
            users = options['data'][0]
            lessons = options['data'][1]
            modules = options['data'][2]
            workshops = options['data'][3]
        except IndexError:
            raise CommandError(
                'python manage.py populate [users] [lessons_per_module] [modules_per_workshop] [workshops]')

        track = create_track(workshops=workshops,
                             modules=modules, lessons=lessons)
        create_users(track, users=users)
        lessons_number = lessons * modules * workshops
        self.stdout.write(self.style.SUCCESS(
            f'Successfully added {users} users and {lessons_number} lessons'))
