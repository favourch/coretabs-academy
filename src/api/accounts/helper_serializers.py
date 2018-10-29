from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class MailingListSerializer(serializers.ModelSerializer):
    address = serializers.EmailField(source='email')
    name = serializers.CharField(source='first_name')

    class Meta:
        model = User
        fields = ('address', 'name')
