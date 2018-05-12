from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin

from . import serializers
from . import models
from django.db import models as django_models

from django.contrib.auth.models import User


class LessonRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.BaseLesson.objects
    serializer_class = serializers.LessonSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset\
            .get_lesson_with_is_shown(self.request.user)\
            .filter(module__slug=self.kwargs.get('module_slug'),
                    slug=self.kwargs.get('slug'))

    def patch(self, request, *args, **kwargs):
        lesson = self.get_object()
        lesson.shown_users.add(request.user)
        return self.partial_update(request, *args, **kwargs)


class WorkshopListAPIView(generics.ListAPIView):
    queryset = models.Workshop.objects.all()
    serializer_class = serializers.WorkshopMainInfoSerializer

    def get_queryset(self):
        return self.queryset.filter(tracks__slug=self.kwargs.get('track_slug'))


class WorkshopRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.WorkshopSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        lessons = django_models.Prefetch(
            'lessons', queryset=models.BaseLesson.objects.get_lesson_with_is_shown(self.request.user))

        modules = django_models.Prefetch(
            'modules', queryset=models.Module.objects.prefetch_related(lessons).all())

        queryset = models.Workshop.objects\
            .prefetch_related(modules)
        # .select_related('authors')\

        return queryset.filter(tracks__slug=self.kwargs.get('track_slug'),
                               slug=self.kwargs.get('slug'))


class TrackListAPIView(generics.ListAPIView):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer


class TrackRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer
    lookup_field = 'slug'
