import factory
from django.db import transaction

from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress
from library.models import Workshop, Track, TrackWorkshop, Module, WorkshopModule, MarkdownLesson

User = get_user_model()


class EmailFactory(factory.DjangoModelFactory):
    class Meta:
        model = EmailAddress

    user = ''
    email = factory.Sequence(lambda n: 'user%d@email.com' % n)
    primary = True
    verified = True


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.Sequence(lambda n: 'user%d@email.com' % n)
    first_name = factory.Faker('name')
    last_name = ''
    is_active = True
    is_superuser = False

    @factory.post_generation
    def lessons(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for lesson in extracted:
                self.lessons.add(lesson)


class WorkshopFactory(factory.DjangoModelFactory):
    class Meta:
        model = Workshop

    title = factory.Sequence(lambda n: 'Workshop%d' % n)
    level = 'beginner'
    last_update_date = factory.Faker('date')
    duration = 50.201
    description = factory.Faker('text')
    used_technologies = factory.Faker('sentence', nb_words=3)
    workshop_result_url = factory.Faker('url')
    workshop_forums_url = factory.Faker('url')


class TrackFactory(factory.DjangoModelFactory):
    class Meta:
        model = Track

    title = 'Track'


class TrackWorkshopFactory(factory.DjangoModelFactory):
    class Meta:
        model = TrackWorkshop

    workshop = ''
    track = ''
    order = factory.Sequence(lambda n: n)


class ModuleFactory(factory.DjangoModelFactory):
    class Meta:
        model = Module

    title = factory.Sequence(lambda n: 'Module%d' % n)


class WorkshopModuleFactory(factory.DjangoModelFactory):
    class Meta:
        model = WorkshopModule

    workshop = ''
    module = ''
    order = factory.Sequence(lambda n: n)


class MarkdownFactory(factory.DjangoModelFactory):
    class Meta:
        model = MarkdownLesson

    title = factory.Sequence(lambda n: 'Lesson%d' % n)
    markdown_url = factory.Faker('url')
    type = 2
    module = ''
    order = factory.Sequence(lambda n: n)

@transaction.atomic
def create_users(track, users=1000):
    lessons = list(MarkdownLesson.objects.all())
    for i in range(users):
        user = UserFactory(lessons=lessons)
        user.profile.track = track
        user.save()
        EmailFactory(user=user, email=user.email)
        print('{} users created'.format(i + 1))


@transaction.atomic
def create_track(track_name='Test Track', workshops=7, modules=5, lessons=5):
    track = TrackFactory(title=track_name)
    for i in range(workshops):
        workshop = WorkshopFactory()
        TrackWorkshopFactory(workshop=workshop, track=track)
        for j in range(modules):
            module = ModuleFactory()
            WorkshopModuleFactory(workshop=workshop, module=module)
            for k in range(lessons):
                MarkdownFactory(module=module)
    return track
