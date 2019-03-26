from ..serializers import serializers, exceptions
from .backends import GithubAPI, GoogleAPI


class SocialSerializer(serializers.Serializer):
    backends = {
        'github': GithubAPI,
        'google': GoogleAPI
    }

    access_token = serializers.CharField(required=True)
    provider = serializers.CharField(required=True)

    def validate_provider(self, provider):
        try:
            self.backend = self.backends[provider]()
            return provider
        except KeyError:
            raise exceptions.ValidationError('Backend Not Found')

    def get_data(self):
        return self.backend, self.validated_data['access_token']
