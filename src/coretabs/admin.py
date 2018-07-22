from django.contrib.admin import AdminSite
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import reverse
from django.views.decorators.cache import never_cache

from rest_framework.authtoken.admin import Token, TokenAdmin
from allauth.account.admin import EmailAddress, EmailAddressAdmin
from django.contrib.auth.admin import User, UserAdmin
from django.contrib.sites.admin import Site, SiteAdmin

from functools import update_wrapper
from django.views.decorators.csrf import csrf_protect


class MyAdminSite(AdminSite):

    @never_cache
    def login(self, request, extra_context=None):
        if request.method == 'GET' and self.has_permission(request):
            # Already logged-in, redirect to admin index
            index_path = reverse('admin:index', current_app=self.name)
            return HttpResponseRedirect(index_path)

        raise Http404

    def admin_view(self, view, cacheable=False):
        def inner(request, *args, **kwargs):
            if not self.has_permission(request):
                raise Http404
            return view(request, *args, **kwargs)

        if not cacheable:
            inner = never_cache(inner)
        # We add csrf_protect here so this function can be used as a utility
        # function for any view, without having to repeat 'csrf_protect'.
        if not getattr(view, 'csrf_exempt', False):
            inner = csrf_protect(inner)
        return update_wrapper(inner, view)


site = MyAdminSite()


# Register Models
site.register(Token, TokenAdmin)
site.register(EmailAddress, EmailAddressAdmin)
site.register(User, UserAdmin)
site.register(Site, SiteAdmin)
