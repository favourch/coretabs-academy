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


class LessonSerializer(serializers.ModelSerializer):
    is_shown = serializers.SerializerMethodField()

    class Meta:
        model = models.BaseLesson
        fields = ('title',
                  'slug',
                  'type',
                  'is_shown')

    def get_is_shown(self, obj):
        # return obj.shown_users.filter(id=self.context['request'].user.id).exists()
        return obj.is_shown(user=self.context['request'].user)


class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = models.Module
        fields = '__all__'


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
