from django.urls import path
from .views import MyProfileView, ProfileView, CertificateView

urlpatterns = [
    path('profile', MyProfileView.as_view(), name='my_profile'),
    path('profiles/<username>', ProfileView.as_view(), name='profile'),
    path('certificates/<uuid>', CertificateView.as_view(), name='certificate'),
]
