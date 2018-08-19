from django.urls import path, include
from . import views


urlpatterns = [
    path('api/v1/auth/logout/', views.logout_view),
    path('api/v1/auth/user/', views.user_details_view),
    path('api/v1/auth/confirmation/', views.resend_confirmation_view),
    path('api/v1/auth/registration/verify-email/', views.verify_email),
]
