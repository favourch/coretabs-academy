'''coretabs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''

from django.urls import path, include
from .admin import site

import debug_toolbar

from . import views


site.site_header = 'Coretabs Admin'
site.site_title = 'Coretabs Admin'
site.index_title = 'Coretabs Admin'

urlpatterns = [

    path('admin/', site.urls),

    path('', include('discourse.urls')),
    path('', include('contact.urls')),
    path('', include('avatars.urls')),

    path('api/v1/', include('library.urls')),
    path('api/v1/auth/', include('accounts.urls')),
    path('api/v1/', include('profiles.urls')),

    path('__debug__/', include(debug_toolbar.urls)),

    path('health/', views.health, name='health')
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
