from django.urls import path
from .views import sso, notifications

urlpatterns = [
    path('api/v1/auth/user/notifications/', notifications),
    path('discourse/sso', sso),
]