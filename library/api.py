from rest_framework import generics

from . import serializers
from . import models


class LessonListAPIView(generics.ListAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer


class ModuleListAPIView(generics.ListAPIView):
    queryset = models.Module.objects.all()
    serializer_class = serializers.ModuleSerializer


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Module.objects.all()
    serializer_class = serializers.ModuleSerializer


class ModuleLessonListAPIView(generics.ListAPIView):
    queryset = models.ModuleLesson.objects.all()
    serializer_class = serializers.ModuleLessonSerializer


class ModuleLessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.ModuleLesson.objects.all()
    serializer_class = serializers.ModuleLessonSerializer


class TrackListAPIView(generics.ListAPIView):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer


class TrackRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer


class TrackModuleListAPIView(generics.ListAPIView):
    queryset = models.TrackModule.objects.all()
    serializer_class = serializers.TrackModuleSerializer


class TrackModuleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.TrackModule.objects.all()
    serializer_class = serializers.TrackModuleSerializer
