import re
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from rest_framework import serializers
from library import models


class LessonMainInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseLesson
        fields = ('title',
                  'slug')


class ModuleMainInfoSerializer(serializers.ModelSerializer):
    lessons = LessonMainInfoSerializer(many=True)

    class Meta:
        model = models.Module
        fields = '__all__'


class WorkshopMainInfoSerializer(serializers.ModelSerializer):
    modules = ModuleMainInfoSerializer(many=True)

    class Meta:
        model = models.Workshop
        fields = ('title',
                  'slug',
                  'level',
                  'description',
                  'modules')


class TrackMainInfoSerializer(serializers.ModelSerializer):
    workshops = WorkshopMainInfoSerializer(many=True)

    class Meta:
        model = models.Track
        fields = '__all__'
