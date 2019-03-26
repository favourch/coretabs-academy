from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSocialAuth(models.Model):
    user = models.ForeignKey(User, related_name='social_auth', on_delete=models.CASCADE)
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=32)
    # avatar_url = models.URLField()

    def __str__(self):
        return f'{self.user}'
