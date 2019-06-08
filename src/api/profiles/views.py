from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView

from django.shortcuts import get_object_or_404
from django.http import Http404

from uuid import UUID

from .models import Profile, Project, Certificate
from .serializers import ProfileSerializer, ProjectSerializer, CertificateSerializer


class MyProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile


class MyProfileProjectsViewSet(ModelViewSet):
    class HisOwnProfile(BasePermission):
        def has_object_permission(self, request, view, obj):
            return obj.is_owner(request.user)

    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, HisOwnProfile)
    def get_queryset(self):
       return Project.objects.filter(profile=self.request.user.profile)


class ProfileView(RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        username = self.kwargs['username']
        obj = get_object_or_404(Profile, user__username=username)
        return obj


class CertificateView(RetrieveAPIView):
    serializer_class = CertificateSerializer

    def get_object(self):
        pk = self.kwargs['uuid']

        try:
            UUID(pk)
        except ValueError:
            raise Http404

        obj = get_object_or_404(Certificate, pk=pk)
        return obj
