from django.db import models as django_models
from . import models as library_models


class WorkshopManager(django_models.Manager):
    def shown_percentage(self, user):
        shown_lessons_count = library_models.BaseLesson.objects.user_shown_lessons(
            user=user).count()
        all_lessons_count = library_models.BaseLesson.objects.count()
        percentage = (shown_lessons_count / all_lessons_count) * 100

        return int(percentage)

    def get_all_workshops(self, user):
        lessons = django_models.Prefetch(
            'lessons', queryset=library_models.BaseLesson.objects.get_lesson_with_is_shown(user))

        modules = django_models.Prefetch(
            'modules', queryset=library_models.Module.objects.prefetch_related(lessons).all())

        return self.get_queryset().prefetch_related(modules)


class BaseLessonManager(django_models.Manager):
    def get_lesson_with_is_shown(self, user):
        return self.get_queryset().annotate(
            is_shown=django_models.Case(django_models.When(shown_users__id=user.id, then=django_models.Value(True)),
                                        default=django_models.Value(False),
                                        output_field=django_models.BooleanField()))
