from django.conf import settings
from django.utils.module_loading import import_string
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from .models import Profile, Project , Certificate, CertificateSignature


class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        return self._choices[obj]


class CountryField(serializers.ChoiceField):
    def to_representation(self, obj):
        if obj:
            return {'text': self._choices[obj], 'value': obj}


class SkillsField(serializers.MultipleChoiceField):
    def to_representation(self, value):
        data = value.split(',')
        result = [
            {'text': lang[1], 'value': lang[0]}
            for lang in Profile.SKILLS_CHOICES if lang[0] in data
        ]

        return result

    def to_internal_value(self, data):
        if isinstance(data, list):
            data = data[0]

        data_list = data.split(',')

        super().to_internal_value(data_list)
        return data


class CertificateSignatureSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='photo.url', read_only=True)

    class Meta:
        model = CertificateSignature
        fields = ('name', 'url')


class CertificateSerializer(serializers.ModelSerializer):
    heading = serializers.CharField(source='template.heading', read_only=True)
    body = serializers.CharField(source='template.body', read_only=True)
    signature = CertificateSignatureSerializer(source='template.signature')

    class Meta:
        model = Certificate
        fields = ('full_name', 'date', 'heading', 'body', 'signature')


class ProfileCertificateSerializer(serializers.ModelSerializer):
    heading = serializers.CharField(source='template.heading')

    class Meta:
        model = Certificate
        fields = ('id', 'date', 'heading')


class ProjectSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    photo = serializers.ImageField(required=False)
    github_link = serializers.RegexField(regex=r'[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)', 
                                                     error_messages={'invalid': _('Invalid Project GitHub URL')},
                                                     allow_blank=True)
    live_demo_link = serializers.RegexField(regex=r'[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)', 
                                                     error_messages={'invalid': _('Invalid Project Demo URL')},
                                                     allow_blank=True)


    def create(self, validated_data):
        user = self.context['request'].user

        instance = Project(profile=user.profile, **validated_data)
        instance.save()

        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    class Meta:
        model = Project
        fields = ('id', 'description', 'photo', 'github_link', 'live_demo_link')


class ProfileSerializer(serializers.ModelSerializer):
    links_errors = {
        'facebook': _('Invalid Facebook URL'),
        'twitter': _('Invalid Twitter URL'),
        'linkedin': _('Invalid LinkedIn URL'),
        'github': _('Invalid Github URL'),
        'website': _('Invalid Website URL'),
    }

    username = serializers.CharField(source='user.username', read_only=True)
    name = serializers.CharField(source='user.first_name', read_only=True)
    role = ChoiceField(Profile.ROLE_CHOICES, read_only=True)
    level = ChoiceField(Profile.LEVEL_CHOICES, read_only=True)
    country = CountryField(Profile.COUNTRY_CHOICES)
    skills = SkillsField(Profile.SKILLS_CHOICES)
    projects = ProjectSerializer(many=True, read_only=True)
    certificates = ProfileCertificateSerializer(many=True, read_only=True)
    date_joined = serializers.DateTimeField(source='user.date_joined')

    facebook_link = serializers.RegexField(regex=r'http(s)?://(www\.)?(facebook|fb)\.com/[A-z0-9_\-\.]+/?',
                                           error_messages={'invalid': links_errors['facebook']},
                                           allow_blank=True)
    twitter_link = serializers.RegexField(regex=r'http(s)?://(www\.)?twitter\.com\/[A-z0-9_]+/?',
                                          error_messages={'invalid': links_errors['twitter']},
                                          allow_blank=True)
    linkedin_link = serializers.RegexField(regex=r'http(s)?://(www\.)?linkedin\.com/in/[A-z0-9_-]+/?',
                                           error_messages={'invalid': links_errors['linkedin']},
                                           allow_blank=True)
    github_link = serializers.RegexField(regex=r'http(s)?://(www\.)?github\.com/[A-z0-9_-]+/?',
                                         error_messages={'invalid': links_errors['github']},
                                         allow_blank=True)
    website_link = serializers.RegexField(regex=r'[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)', 
                                         error_messages={'invalid': _('Invalid Website URL')},
                                         allow_blank=True)

    avatar_url = serializers.SerializerMethodField()

    def get_avatar_url(self, obj, size=settings.AVATAR_DEFAULT_SIZE):
        for provider_path in settings.AVATAR_PROVIDERS:
            provider = import_string(provider_path)
            avatar_url = provider.get_avatar_url(obj.user, size)
            if avatar_url:
                return avatar_url

    class Meta:
        model = Profile
        fields = ('username', 'name', 'role', 'level', 'description',
                  'country', 'bio', 'skills', 'projects', 'certificates', 'avatar_url',
                  'facebook_link', 'twitter_link', 'linkedin_link', 'github_link',
                  'website_link', 'date_joined')
