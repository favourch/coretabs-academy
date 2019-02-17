from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from .models import Profile, Certificate


class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        return self._choices[obj]


class MultipleChoiceField(serializers.MultipleChoiceField):
    def to_representation(self, value):
        result = value.split(',')
        return result

    def to_internal_value(self, data):
        super().to_internal_value(data)
        result = ",".join(data)
        return result


class CertificateSerializer(serializers.ModelSerializer):
    heading = serializers.CharField(source='template.heading', read_only=True)
    body = serializers.CharField(source='template.body', read_only=True)
    signature = serializers.CharField(source='template.signature.photo.url', read_only=True)

    class Meta:
        model = Certificate
        fields = ('full_name', 'date', 'heading', 'body', 'signature')


class ProfileCertificateSerializer(serializers.ModelSerializer):
    heading = serializers.CharField(source='template.heading')

    class Meta:
        model = Certificate
        fields = ('date', 'heading')


class ProfileSerializer(serializers.ModelSerializer):
    links_errors = {
        'facebook': _('Invalid Facebook url'),
        'twitter': _('Invalid Twitter url'),
        'linkedin': _('Invalid LinkedIn url'),
        'website': _('Invalid Website url'),
    }

    username = serializers.CharField(source='user.username', read_only=True)
    name = serializers.CharField(source='user.first_name', read_only=True)
    role = ChoiceField(Profile.ROLE_CHOICES, read_only=True)
    level = ChoiceField(Profile.LEVEL_CHOICES, read_only=True)
    country = ChoiceField(Profile.COUNTRY_CHOICES)

    languages = MultipleChoiceField(Profile.LANGUAGES_CHOICES)

    certificates = ProfileCertificateSerializer(many=True, read_only=True)

    facebook_link = serializers.RegexField(regex=r'http(s)?://(www\.)?(facebook|fb)\.com/[A-z0-9_\-\.]+/?',
                                           error_messages={'invalid': links_errors['facebook']},
                                           allow_blank=True)
    twitter_link = serializers.RegexField(regex=r'http(s)?://(.*\.)?twitter\.com\/[A-z0-9_]+/?',
                                          error_messages={'invalid': links_errors['twitter']},
                                          allow_blank=True)
    linkedin_link = serializers.RegexField(regex=r'http(s)?://([\w]+\.)?linkedin\.com/in/[A-z0-9_-]+/?',
                                           error_messages={'invalid': links_errors['linkedin']},
                                           allow_blank=True)
    website_link = serializers.URLField(error_messages={'invalid': links_errors['website']},
                                        allow_blank=True)

    class Meta:
        model = Profile
        fields = ('username', 'name', 'role', 'level', 'description',
                  'country', 'bio', 'languages', 'certificates',
                  'facebook_link', 'twitter_link', 'linkedin_link', 'website_link')

        read_only_fields = ('description',)
