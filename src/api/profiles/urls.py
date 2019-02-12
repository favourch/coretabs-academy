from django.urls import path
from .views import ProfileView, CertificateView

urlpatterns = [
    path('profiles/<username>', ProfileView.as_view(), name='profile'),
    path('certificates/<uuid>', CertificateView.as_view(), name='certificate'),
]
