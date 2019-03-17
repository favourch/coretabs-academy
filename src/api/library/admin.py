from django.contrib import admin
from coretabs.admin import site
from . import models
from . import custom_filters

from adminsortable2.admin import SortableInlineAdminMixin


class LessonAdmin(admin.ModelAdmin):
    list_filter = [
        custom_filters.LessonsByModuleListFilter,
        custom_filters.LessonsByWorkshopListFilter,
        custom_filters.LessonsByTrackListFilter
    ]
    ordering = ['-last_update_date']


class ModuleLessonInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.BaseLesson
    extra = 1

    def get_queryset(self, request):
        return self.model.objects.select_subclasses()


class ModuleAdmin(admin.ModelAdmin):
    inlines = (ModuleLessonInline,)
    list_filter = [
        custom_filters.ModulesByWorkshopListFilter,
        custom_filters.ModuleByTrackListFilter
    ]
    ordering = ['-last_update_date']


class WorkshopModuleInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.WorkshopModule
    extra = 1


class WorkshopAdmin(admin.ModelAdmin):
    inlines = (WorkshopModuleInline,)
    list_filter = [custom_filters.WorkshopByTrackListFilter]
    ordering = ['-last_update_date']


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
