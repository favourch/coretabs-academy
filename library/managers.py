from django.db import models

from . import models as lib_models

from decimal import Decimal


class WorkshopManager(models.Manager):
    def shown_percentage(self, user, workshop):
              
        q = lib_models.Workshop.objects.annotate(
            shown_count=models.Count(
                'modules__lessons',
                 filter=models.Q(modules__lessons__shown_users__id=user.id)),

            total_count=models.Count('modules__lessons'),

            percentage=models.ExpressionWrapper(
                (models.F('shown_count') * Decimal('1.0') / models.F('total_count')) * 100,
            output_field=models.FloatField())
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
    def get_lesson_with_is_shown(self, user):
        return self.get_queryset().annotate(
            is_shown=models.Case(models.When(shown_users__id=user.id, then=models.Value(True)),
                                 default=models.Value(False),
                                 output_field=models.BooleanField()))
