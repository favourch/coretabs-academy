from rest_framework.fields import CurrentUserDefault
from rest_framework import serializers

from . import models


class LessonSerializer(serializers.ModelSerializer):
    is_shown = serializers.SerializerMethodField()

    class Meta:
        model = models.Lesson
        fields = ('title',
                  'slug',
                  'type',
                  'url',
                  'is_shown')

    def get_is_shown(self, obj):
        # return obj.lessons.filter(shown_users__user_id=CurrentUserDefault().user.id).exists()
        return obj.shown_users.filter(id=1).exists()


class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = models.Module
        fields = '__all__'


# class ModuleLessonSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = models.ModuleLesson
#        fields = '__all__'

class WorkshopSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True)

    class Meta:
        model = models.Workshop
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    workshops = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='slug')

    class Meta:
        model = models.Track
        fields = '__all__'


# class TrackModuleSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = models.TrackModule
#        fields = '__all__'
