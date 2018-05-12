from django.db import models
from . import models as lib_models


class WorkshopManager(models.Manager):
    def shown_percentage(self, user):
        shown_lessons_count = lib_models.BaseLesson.objects.user_shown_lessons(
            user=user).count()
        all_lessons_count = lib_models.BaseLesson.objects.count()
        percentage = (shown_lessons_count / all_lessons_count) * 100

        return percentage

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
    def user_shown_lessons(self, user):
        return self.get_queryset().filter(shown_users__id=1)
