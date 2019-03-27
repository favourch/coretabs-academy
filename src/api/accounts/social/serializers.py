from rest_framework import serializers
from rest_framework.exceptions import ParseError
from .backends import GithubAPI, GoogleAPI


class SocialSerializer(serializers.Serializer):
    backends = {
        'github': GithubAPI,
        'google': GoogleAPI
    }

    access_token = serializers.CharField(required=True)
    provider = serializers.CharField(required=True)

    def get_data(self):
        provider = self.validated_data['provider']
        access_token = self.validated_data['access_token']

        try:
            backend = self.backends[provider]()
            return backend, access_token

        except KeyError:
            raise ParseError('provider not found')
