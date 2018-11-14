from rest_framework.generics import RetrieveUpdateAPIView
from django.shortcuts import get_object_or_404
from .models import Profile
from .serializers import ProfileSerializer


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        username = self.kwargs['username']
        obj = get_object_or_404(Profile, user__username=username)
        return obj
