from django.dispatch import receiver

from django.db.models.signals import post_save
from accounts.signals import user_updated
from django.contrib.auth.signals import user_logged_out

from .tasks import discourse_sync_sso, discourse_logout
from django.contrib.auth import get_user_model
User = get_user_model()


@receiver(post_save, sender=User)
def discourse_create_user(sender, instance, created, **kwargs):
    if created:
        discourse_sync_sso(instance.id)


@receiver(user_updated)
def discourse_update_user(sender, user, **kwargs):
    discourse_sync_sso(user.id)


@receiver(user_logged_out)
def discourse_logout_handler(sender, user, request, **kwargs):
    discourse_logout(user.id)


# TODO
# @receiver(post_delete, sender=User)
# def discourse_delete_user_handler(sender, instance, created, **kwargs):
#     discourse_delete_user(instance.id)
