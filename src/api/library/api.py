from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsApproved

from . import serializers
from . import models
from django.db import models as django_models


class BaseLessonListAPIView(generics.ListAPIView):
    queryset = models.BaseLesson.objects.all()
    serializer_class = serializers.BaseLessonSerializer

    def get_queryset(self):
        return self.queryset.filter(module__slug=self.kwargs.get('module_slug'))


class BaseLessonRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.BaseLesson.objects
    serializer_class = serializers.BaseLessonSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticated, IsApproved)

    def get_queryset(self):
        return self.queryset.with_is_shown(self.request.user).select_subclasses().filter(
            module__slug=self.kwargs.get('module_slug'), slug=self.kwargs.get('slug'))

    def put(self, request, *args, **kwargs):
        lesson = self.get_object()
        user = request.user

        lesson.shown_users.add(user)

        lesson_exist_in_track = lesson.module.workshops.filter(
            tracks__id=user.account.track.id).first() is not None

        if lesson_exist_in_track:
            user.account.last_opened_lesson = lesson
            user.account.save()

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
    queryset = models.Workshop.objects
    lookup_field = 'slug'
    serializer_class = serializers.WorkshopsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user

        lessons = django_models.Prefetch(
            'lessons', queryset=models.BaseLesson.objects.select_subclasses())

        modules = django_models.Prefetch(
            'modules', queryset=models.Module.objects.prefetch_related(lessons).all())

        return self.queryset.get_workshops(user).prefetch_related(modules).filter(
            tracks__slug=self.kwargs.get('track_slug'))


class WorkshopRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Workshop.objects
    lookup_field = 'slug'
    serializer_class = serializers.WorkshopSerializer
    permission_classes = (IsAuthenticated, IsApproved)

    def get_queryset(self):
        user = self.request.user

        lessons = django_models.Prefetch(
            'lessons', queryset=models.BaseLesson.objects.with_is_shown(user).select_subclasses())

        modules = django_models.Prefetch(
            'modules', queryset=models.Module.objects.prefetch_related(lessons).all())

        return self.queryset.get_workshops(user).filter(slug=self.kwargs.get('slug')).prefetch_related(modules).filter(
            tracks__slug=self.kwargs.get('track_slug'))


class TrackListAPIView(generics.ListAPIView):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer


class TrackRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Track.objects
    serializer_class = serializers.TrackMainInfoSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        lessons = django_models.Prefetch(
            'lessons', queryset=models.BaseLesson.objects.select_subclasses())

        modules = django_models.Prefetch(
            'modules', queryset=models.Module.objects.prefetch_related(lessons).all())

        workshops = django_models.Prefetch(
            'workshops', queryset=models.Workshop.objects.prefetch_related(modules)
            .filter(tracks__slug=self.kwargs.get('slug')))

        return self.queryset.prefetch_related(workshops).all()
