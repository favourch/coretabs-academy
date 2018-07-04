from django.db import models as django_models
from . import models as library_models

from decimal import Decimal
from model_utils.managers import InheritanceManager

from caching.base import CachingManager


class WorkshopManager(CachingManager):
    def shown_percentage(self, user, workshop):

        q = library_models.Workshop.objects.annotate(
            shown_count=django_models.Count(
                'modules__lessons',
                filter=django_models.Q(modules__lessons__shown_users__id=user.id)),

            total_count=django_models.Count('modules__lessons'),

            percentage=django_models.ExpressionWrapper(
                (django_models.F('shown_count') * Decimal('1.0') /
                 django_models.F('total_count')) * 100,
                output_field=django_models.FloatField())
        )

        return q.get(id=workshop.id).percentage

    def get_all_workshops(self, user):
        lessons = django_models.Prefetch(
            'lessons', queryset=library_models.BaseLesson.objects.get_lesson_with_is_shown(user).select_subclasses())

        modules = django_models.Prefetch(
            'modules', queryset=library_models.Module.objects.prefetch_related(lessons).all())

        return self.get_queryset().prefetch_related(modules)


class BaseLessonManager(InheritanceManager, CachingManager):
    def get_lesson_with_is_shown(self, user):

        user_shown_lessons = user.lessons.values('id')

        shown_user_case = django_models.Case(
            django_models.When(id__in=user_shown_lessons,
                               then=django_models.Value(True)),
            default=django_models.Value(False),
            output_field=django_models.BooleanField())

        return self.get_queryset().annotate(
            is_shown=shown_user_case)
