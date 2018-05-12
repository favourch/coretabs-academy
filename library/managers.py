from django.db import models

from . import models as lib_models


class WorkshopManager(models.Manager):
    def shown_percentage(self, user, workshop):
              
        q = lib_models.Workshop.objects.annotate(
            percentage=(
                models.Count('modules__lessons', filter=models.Q(modules__lessons__shown_users__id=user.id)) / 
                models.Count('modules__lessons')) * 100
        )

        return q.get(id=workshop.id).percentage

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
