from django.contrib import admin
from coretabs.admin import site
from . import models

from adminsortable2.admin import SortableInlineAdminMixin


class ModuleLessonInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.BaseLesson
    extra = 1

    def get_queryset(self, request):
        return self.model.objects.select_subclasses()


class ModuleAdmin(admin.ModelAdmin):
    inlines = (ModuleLessonInline,)


class WorkshopModuleInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.WorkshopModule
    extra = 1


class WorkshopAdmin(admin.ModelAdmin):
    inlines = (WorkshopModuleInline,)


class TrackWorkshopInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.TrackWorkshop
    extra = 1


class TrackAdmin(admin.ModelAdmin):
    inlines = (TrackWorkshopInline,)


site.register(models.MarkdownLesson)
site.register(models.QuizLesson)
site.register(models.VideoLesson)
site.register(models.Module, ModuleAdmin)
site.register(models.WorkshopModule)
site.register(models.Workshop, WorkshopAdmin)
site.register(models.TrackWorkshop)
site.register(models.Track, TrackAdmin)
