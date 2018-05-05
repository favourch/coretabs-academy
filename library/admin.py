from django.contrib import admin
from . import models


admin.site.register(models.Lesson)
admin.site.register(models.ModuleLesson)
admin.site.register(models.Module)
admin.site.register(models.Workshop)
admin.site.register(models.WorkshopModule)
admin.site.register(models.Track)
admin.site.register(models.TrackWorkshop)
