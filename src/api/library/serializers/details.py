from django.contrib.auth import get_user_model

from rest_framework import serializers
from library import models

from django.conf import settings
from django.utils.module_loading import import_string


class AuthorSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    name = serializers.CharField(source='first_name',
                                 max_length=100,
                                 min_length=5,
                                 required=True)

    class Meta:
        model = get_user_model()
        fields = ('name', 'role', 'avatar_url')

    def get_role(self, obj):
        return obj.profile.role

    def get_avatar_url(self, obj, size=settings.AVATAR_DEFAULT_SIZE):
        for provider_path in settings.AVATAR_PROVIDERS:
            provider = import_string(provider_path)
            avatar_url = provider.get_avatar_url(obj, size)
            if avatar_url:
                return avatar_url


class BaseLessonSerializer(serializers.ModelSerializer):
    is_shown = serializers.BooleanField()

    def to_representation(self, instance):
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
    is_shown = serializers.BooleanField(default=False)

    class Meta:
        model = models.MarkdownLesson
        fields = ('title',
                  'slug',
                  'type',
                  'markdown_url',
                  'is_shown')


class VideoLessonSerializer(serializers.ModelSerializer):
    is_shown = serializers.BooleanField(default=False)

    class Meta:
        model = models.VideoLesson
        fields = ('title',
                  'slug',
                  'type',
                  'video_url',
                  'markdown_url',
                  'is_shown')


class QuizLessonSerializer(serializers.ModelSerializer):
    is_shown = serializers.BooleanField(default=False)

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


class WorkshopsSerializer(serializers.ModelSerializer):
    shown_percentage = serializers.FloatField()
    modules = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='slug')

    class Meta:
        model = models.Workshop
        fields = ('title',
                  'slug',
                  'modules',
                  'shown_percentage')


class WorkshopSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source='get_level_display')
    shown_percentage = serializers.IntegerField()
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


class TrackSerializer(serializers.ModelSerializer):
    workshops = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='slug')

    class Meta:
        model = models.Track
        fields = '__all__'
