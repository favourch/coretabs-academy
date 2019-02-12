from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404
from .models import Profile, Certificate
from .serializers import ProfileSerializer, CertificateSerializer


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        username = self.kwargs['username']
        obj = get_object_or_404(Profile, user__username=username)
        return obj


class CertificateView(RetrieveAPIView):
    serializer_class = CertificateSerializer

    def get_object(self):
        pk = self.kwargs['uuid']
        obj = get_object_or_404(Certificate, pk=pk)
        return obj
