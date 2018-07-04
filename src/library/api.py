from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin

from . import serializers
from . import models
from django.db import models as django_models

from django.contrib.auth.models import User


class BaseLessonListAPIView(generics.ListAPIView):
    queryset = models.BaseLesson.objects.all()
    serializer_class = serializers.BaseLessonSerializer

    def get_queryset(self):
        return self.queryset.filter(module__slug=self.kwargs.get('module_slug'))


class BaseLessonRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.BaseLesson.objects
    serializer_class = serializers.BaseLessonSerializer
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
    lookup_field = 'slug'
    serializer_class = serializers.WorkshopMainInfoSerializer

    def get_queryset(self):

        lessons = django_models.Prefetch(
            'lessons', queryset=models.BaseLesson.objects.select_subclasses())

        modules = django_models.Prefetch(
            'modules', queryset=models.Module.objects.prefetch_related(lessons).all())

        return self.queryset.prefetch_related(modules).filter(tracks__slug=self.kwargs.get('track_slug'))


class WorkshopRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Workshop.objects.all()
    lookup_field = 'slug'
    serializer_class = serializers.WorkshopSerializer

    def get_queryset(self):
        user = self.request.user

        lessons = django_models.Prefetch(
            'lessons', queryset=models.BaseLesson.objects.get_lesson_with_is_shown(user).select_subclasses())

        modules = django_models.Prefetch(
            'modules', queryset=models.Module.objects.prefetch_related(lessons).all())

        return self.queryset.prefetch_related(modules).filter(tracks__slug=self.kwargs.get('track_slug'))


class TrackListAPIView(generics.ListAPIView):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer


class TrackRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer
    lookup_field = 'slug'
