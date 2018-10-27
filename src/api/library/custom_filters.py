from django.contrib import admin
from library import models

# TODO: try to make base filter class
class BaseLibraryListFilter(admin.SimpleListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'
    title = 'BaseLibray'
    dropdown_objects = None
    action_lookup = None
    parameter_name = 'by_module'

    def lookups(self, request, model_admin):
        tupleObj = ()
        for obj in self.dropdown_objects:
            tupleData = None
            tupleData = (obj.id, obj.title)
            tupleObj = tupleObj +(tupleData,)

        return tupleObj


class LessonsByModuleListFilter(BaseLibraryListFilter):
    title = 'Module'
    dropdown_objects = models.Module.objects.all()

    def queryset(self, request, queryset):
        
        obj_id = self.value()
        if obj_id is None: return queryset

        return queryset.filter(module=obj_id)
