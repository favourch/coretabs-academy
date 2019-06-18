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
        fields = ('title',
                  'slug',
                  'created_date',
                  'last_update_date',
                  'lessons')


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
        fields = ('title',
                  'slug',
                  'workshops')
