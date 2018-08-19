from django.urls import path
from . import views

urlpatterns = [
    path('discourse/sso/', views.sso),
    path('api/v1/auth/user/notifications/',
         discourse_views.notifications),
]
