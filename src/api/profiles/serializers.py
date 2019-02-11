from rest_framework import serializers
from .models import Profile, Team, Certificate


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'members')


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    name = serializers.CharField(source='user.first_name', read_only=True)
    team = TeamSerializer()

    class Meta:
        model = Profile
        fields = ('username', 'name', 'role', 'level', 'description', 'available_for_work',
                  'country', 'city', 'bio', 'skills', 'preferred_skills', 'languages', 'team', 'certificates')


class CertificateSerializer(serializers.ModelSerializer):
    heading = serializers.CharField(source='template.heading', read_only=True)
    body = serializers.CharField(source='template.body', read_only=True)
    signature = serializers.CharField(source='template.signature.photo.url', read_only=True)

    class Meta:
        model = Certificate
        fields = ('full_name', 'date', 'heading', 'body', 'signature')
