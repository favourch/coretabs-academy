import re
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from . import models

from hacks.serializers import UserDetailsSerializer


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


class BaseLessonSerializer(serializers.ModelSerializer):
    is_shown = serializers.BooleanField()

    class Meta:
        model = models.BaseLesson
        fields = ('title',
                  'slug',
                  'type',
                  'is_shown')

    def get_is_shown(self, obj):
        return obj.is_shown(user=self.context['request'].user)


class MarkdownLessonSerializer(BaseLessonSerializer):
    class Meta(BaseLessonSerializer.Meta):
        model = models.MarkdownLesson
        fields = ('title',
                  'slug',
                  'type',
                  'is_shown',
                  'markdown_url')


class VideoLessonSerializer(BaseLessonSerializer):
    class Meta(BaseLessonSerializer.Meta):
        model = models.MarkdownLesson
        fields = ('title',
                  'slug',
                  'type',
                  'is_shown',
                  'video_url',
                  'markdown_url')


class QuizLessonSerializer(BaseLessonSerializer):
    class Meta(BaseLessonSerializer.Meta):
        model = models.MarkdownLesson
        fields = ('title',
                  'slug',
                  'type',
                  'is_shown',
                  'markdown_url')



class ModuleSerializer(serializers.ModelSerializer):
    lessons = BaseLessonSerializer(many=True)

    class Meta:
        model = models.Module
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer()

    class Meta:
        model = models.User
        fields = ('name')


class WorkshopSerializer(serializers.ModelSerializer):
    shown_percentage = serializers.SerializerMethodField()
    modules = ModuleSerializer(many=True)
    #authors = AuthorSerializer(many=True)

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
