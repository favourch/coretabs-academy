from django.db import models
from . import models as lib_models


class WorkshopManager(models.Manager):
    def shown_percentage(self, user):
        shown_lessons_count = lib_models.BaseLesson.objects.user_shown_lessons(user=user).count()
        all_lessons_count = lib_models.BaseLesson.objects.count()
        percentage = (shown_lessons_count / all_lessons_count) * 100

        return percentage
