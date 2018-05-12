from django.db import models
from . import models as lib_models


class WorkshopManager(models.Manager):
    def shown_percentage(self, user):
        shown_lessons_count = lib_models.BaseLesson.objects.user_shown_lessons(
            user=user).count()
        all_lessons_count = lib_models.BaseLesson.objects.count()
        percentage = (shown_lessons_count / all_lessons_count) * 100

        return int(percentage)

    def get_all_workshops_with_modules_and_lessons(self, user):
        # workshops = lib_models.Workshop.objects.prefetch_related(
        #    models.Prefetch(
        #        'modules',
        #        queryset=lib_models.Module.objects.prefetch_related(
        #            models.Prefetch(
        #                'lessons',
        #                queryset=lib_models.BaseLesson.objects.user_shown_lessons(
        #                    user)
        #            )),
        #    ))

        workshops = lib_models.Workshop.objects.prefetch_related(
            'modules', 'modules__lessons')
        #modules = workshops.modules
        #lessons = modules.lessons

        return workshops


class BaseLessonManager(models.Manager):
    def get_lesson_with_is_shown(self, user):
        return self.get_queryset().annotate(
            is_shown=models.Case(models.When(shown_users__id=user.id, then=models.Value(True)),
                                 default=models.Value(False),
                                 output_field=models.BooleanField()))
