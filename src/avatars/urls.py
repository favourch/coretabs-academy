from django.urls import path, include
from . import views


urlpatterns = [
    path('api/v1/auth/user/avatar/', views.upload_avatar_view)
]
