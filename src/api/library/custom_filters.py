from django.contrib import admin
from library import models


class BaseLibraryListFilter(admin.SimpleListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'
    title = 'BaseLibray'
    dropdown_objects = None
    action_lookup = None
    parameter_name = 'no_filter'

    def lookups(self, request, model_admin):
        tupleObj = ()
        for obj in self.dropdown_objects:
            tupleData = None
            tupleData = (obj.id, obj.title)
            tupleObj = tupleObj +(tupleData,)

        return tupleObj


class LessonsByModuleListFilter(BaseLibraryListFilter):
    title = 'Module'
    parameter_name = 'by_module'
    dropdown_objects = models.Module.objects.all()

    def queryset(self, request, queryset):
        obj_id = self.value()
        if obj_id is None: return queryset

        return queryset.filter(module=obj_id)


class LessonsByWorkshopListFilter(BaseLibraryListFilter): 
    title = 'Workshop'
    parameter_name = 'by_workshop'
    dropdown_objects = models.Workshop.objects.all()

    def queryset(self, request, queryset):
        obj_id = self.value()
        if obj_id is None: 
            return queryset

        return queryset.filter(module__workshops=obj_id)


class LessonsByTrackListFilter(BaseLibraryListFilter): 
    title = 'Track'
    parameter_name = 'by_track'
    dropdown_objects = models.Track.objects.all()

    def queryset(self, request, queryset):
        obj_id = self.value()
        if obj_id is None: 
            return queryset

        return queryset.filter(module__workshops__tracks=obj_id)


class ModulesByWorkshopListFilter(BaseLibraryListFilter): 
    title = 'Workshop'
    parameter_name = 'by_workshop'
    dropdown_objects = models.Workshop.objects.all()

    def queryset(self, request, queryset):
        obj_id = self.value()
        if obj_id is None: 
            return queryset

        return queryset.filter(workshops=obj_id)


class ModuleByTrackListFilter(BaseLibraryListFilter): 
    title = 'Track'
    parameter_name = 'by_track'
    dropdown_objects = models.Track.objects.all()

    def queryset(self, request, queryset):
        obj_id = self.value()
        if obj_id is None: 
            return queryset

        return queryset.filter(workshops__tracks=obj_id)


class WorkshopByTrackListFilter(BaseLibraryListFilter): 
    title = 'Track'
    parameter_name = 'by_track'
    dropdown_objects = models.Track.objects.all()

    def queryset(self, request, queryset):
        obj_id = self.value()
        if obj_id is None: 
            return queryset

        return queryset.filter(tracks=obj_id)
