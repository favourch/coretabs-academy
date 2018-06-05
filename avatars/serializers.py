import os

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from django.conf import settings

from avatar.models import Avatar
from avatar.signals import avatar_updated


class UploadAvatarSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Avatar
        fields = ('avatar', 'avatar_url',)

    def get_avatar_url(self, obj):
        return obj.avatar_set.get(primary=True).get_absolute_url()
    
    def validate_avatar(self, avatar):
        if settings.AVATAR_ALLOWED_FILE_EXTS:
            root, ext = os.path.splitext(avatar.name.lower())
            if ext not in settings.AVATAR_ALLOWED_FILE_EXTS:
                raise serializers.ValidationError(_("invalid file extension."))

        if avatar.size > settings.AVATAR_MAX_SIZE:
            raise serializers.ValidationError("Your file is too big")

    def save(self, *args, **kwargs):
        request = self.context.get('request')
        user = request.user
        if 'avatar' in request.FILES:
            avatar = Avatar(user=user, primary=True)
            image_file = request.FILES['avatar']
            avatar.avatar.save(image_file.name, image_file)
            avatar.save()
            avatar_updated.send(sender=Avatar, user=user, avatar=avatar)
        return user
