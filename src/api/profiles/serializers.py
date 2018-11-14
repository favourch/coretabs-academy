from rest_framework import serializers
from .models import Profile, Team


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
                  'country', 'city', 'bio', 'skills', 'preferred_skills', 'languages', 'team')
