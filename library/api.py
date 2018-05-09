from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin

from . import serializers
from . import models


class LessonListAPIView(generics.ListAPIView):
    queryset = models.BaseLesson.objects.all()
    serializer_class = serializers.LessonSerializer

    def get_queryset(self):
        return self.queryset.filter(modules__slug=self.kwargs.get('module_slug'))


class LessonRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.BaseLesson.objects.all()
    serializer_class = serializers.LessonSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset.filter(modules__slug=self.kwargs.get('module_slug'),
                                    slug=self.kwargs.get('slug'))

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ModuleListAPIView(generics.ListAPIView):
    queryset = models.Module.objects.all()
    serializer_class = serializers.ModuleSerializer

    def get_queryset(self):
        return self.queryset.filter(workshops__slug=self.kwargs.get('workshop_slug'))


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Module.objects.all()
    serializer_class = serializers.ModuleSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset.filter(workshops__slug=self.kwargs.get('workshop_slug'),
                                    slug=self.kwargs.get('slug'))


class WorkshopListAPIView(generics.ListAPIView):
    queryset = models.Workshop.objects.all()
    serializer_class = serializers.WorkshopSerializer

    def get_queryset(self):
        return self.queryset.filter(tracks__slug=self.kwargs.get('track_slug'))


class WorkshopRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Workshop.objects.all()
    serializer_class = serializers.WorkshopSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset.filter(tracks__slug=self.kwargs.get('track_slug'),
                                    slug=self.kwargs.get('slug'))


class TrackListAPIView(generics.ListAPIView):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer


class TrackRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer
    lookup_field = 'slug'
