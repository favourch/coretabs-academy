from django.contrib import admin
from library.models import Module


class LessonsByModuleListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'
    title = 'Module'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'by_module'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """

        modules = None
        tupleObj = ()
        modules = Module.objects.all()

        for module in modules:
            tupleData = None
            tupleData = (module.id, module.title)
            tupleObj = tupleObj +(tupleData,)

        return tupleObj

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        module_id = self.value()
        if module_id is not None:
            return queryset.filter(module=self.value())
        else:
            return queryset