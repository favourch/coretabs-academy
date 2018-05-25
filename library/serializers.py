import re
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from rest_framework import serializers
from . import models


class WorkshopMainInfoSerializer(serializers.ModelSerializer):

    class ModuleMainInfoSerializer(serializers.ModelSerializer):

        class LessonMainInfoSerializer(serializers.ModelSerializer):

            class Meta:
                model = models.BaseLesson
                fields = ('title',
                          'slug')

        lessons = LessonMainInfoSerializer(many=True)

        class Meta:
            model = models.Module
            fields = '__all__'

    modules = ModuleMainInfoSerializer(many=True)

    class Meta:
        model = models.Workshop
        fields = ('title',
                  'slug',
                  'modules',
                  'description')


class ProfileSerializer(serializers.ModelSerializer):
    track = serializers.SerializerMethodField()
    last_opened_workshop = serializers.SerializerMethodField()
    last_opened_module = serializers.SerializerMethodField()
    last_opened_lesson = serializers.SerializerMethodField()

    class Meta:
        model = models.Profile
        fields = ('role',
                  'track',
                  'last_opened_workshop',
                  'last_opened_module',
                  'last_opened_lesson')

    def get_track(self, obj):
        return obj.track.slug

    def get_last_opened_workshop(self, obj):
        return obj.last_opened_lesson.module.workshops.filter(tracks__id=obj.track.id).first().slug

    def get_last_opened_module(self, obj):
        return obj.last_opened_lesson.module.slug

    def get_last_opened_lesson(self, obj):
        return obj.last_opened_lesson.slug


class AuthorSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    name = serializers.CharField(source='first_name',
                                 max_length=100,
                                 min_length=5,
                                 required=True)

    class Meta:
        model = get_user_model()
        fields = ('name', 'role')

    def get_role(self, obj):
        return obj.profile.role


class BaseLessonSerializer(serializers.ModelSerializer):
    is_shown = serializers.BooleanField()

    def to_representation(self, instance):
        print(instance.type == models.BaseLesson.MARKDOWN)
        if instance.type == models.BaseLesson.MARKDOWN:
            return MarkdownLessonSerializer(instance=instance).data
        elif instance.type == models.BaseLesson.QUIZ:
            return QuizLessonSerializer(instance=instance).data
        elif instance.type == models.BaseLesson.SCRIMBA_VIDEO or instance.type == models.BaseLesson.YOUTUBE_VIDEO:
            return VideoLessonSerializer(instance=instance).data

    class Meta:
        model = models.BaseLesson
        fields = ('title',
                  'slug',
                  'type',
                  'is_shown')


class MarkdownLessonSerializer(serializers.ModelSerializer):
    is_shown = serializers.BooleanField()

    class Meta:
        model = models.MarkdownLesson
        fields = ('title',
                  'slug',
                  'type',
                  'markdown_url',
                  'is_shown')


class VideoLessonSerializer(serializers.ModelSerializer):
    is_shown = serializers.BooleanField()

    class Meta:
        model = models.VideoLesson
        fields = ('title',
                  'slug',
                  'type',
                  'video_url',
                  'markdown_url',
                  'is_shown')


class QuizLessonSerializer(serializers.ModelSerializer):
    is_shown = serializers.BooleanField()

    class Meta:
        model = models.QuizLesson
        fields = ('title',
                  'slug',
                  'type',
                  'markdown_url',
                  'is_shown')


class ModuleSerializer(serializers.ModelSerializer):
    lessons = BaseLessonSerializer(many=True)

    class Meta:
        model = models.Module
        fields = '__all__'


class WorkshopSerializer(serializers.ModelSerializer):
    shown_percentage = serializers.SerializerMethodField()
    modules = ModuleSerializer(many=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = models.Workshop
        fields = ('title',
                  'slug',
                  'level',
                  'last_update_date',
                  'duration',
                  'description',
                  'used_technologies',
                  'workshop_result_url',
                  'workshop_forums_url',
                  'authors',
                  'modules',
                  'shown_percentage')

    def get_shown_percentage(self, obj):
        return int(obj.shown_percentage(user=self.context['request'].user, workshop=obj))


class TrackSerializer(serializers.ModelSerializer):
    workshops = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='slug')

    class Meta:
        model = models.Track
        fields = '__all__'
