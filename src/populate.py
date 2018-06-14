import factory
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress
from library.models import Workshop, Track, TrackWorkshop, Module, WorkshopModule, MarkdownLesson

User = get_user_model()


class EmailFactory(factory.Factory):
    class Meta:
        model = EmailAddress

    user = ''
    email = factory.Sequence(lambda n: 'user%d@email.com' % n)
    primary = True
    verified = True


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.Sequence(lambda n: 'user%d@email.com' % n)
    first_name = factory.Faker('name')
    last_name = ''
    is_active = True
    is_superuser = False


class WorkshopFactory(factory.Factory):
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


class TrackFactory(factory.Factory):
    class Meta:
        model = Track

    title = 'Track'


class TrackWorkshopFactory(factory.Factory):
    class Meta:
        model = TrackWorkshop

    workshop = ''
    track = ''
    order = factory.Sequence(lambda n: n)


class ModuleFactory(factory.Factory):
    class Meta:
        model = Module

    title = 'Module'


class WorkshopModuleFactory(factory.Factory):
    class Meta:
        model = WorkshopModule

    workshop = ''
    module = ''
    order = factory.Sequence(lambda n: n)


class MarkdownFactory(factory.Factory):
    class Meta:
        model = MarkdownLesson

    title = factory.Sequence(lambda n: 'lesson %d' % n)
    markdown_url = factory.Faker('url')
    type = 0
    module = ''
    order = factory.Sequence(lambda n: n)


def create_users(users=1000):
    for i in range(users):
        user = UserFactory()
        user.save()
        email = EmailFactory(user=user, email=user.email)
        email.save()


def create_track(track_name='Test Track', workshops=7, modules=5, lessons=5):
    track = TrackFactory(title=track_name)
    track.save()
    for i in range(workshops):
        workshop = WorkshopFactory()
        workshop.save()
        TrackWorkshopFactory(workshop=workshop, track=track).save()
        for j in range(modules):
            module = ModuleFactory()
            module.save()
            WorkshopModuleFactory(workshop=workshop, module=module).save()
            for k in range(lessons):
                MarkdownFactory(module=module).save()
