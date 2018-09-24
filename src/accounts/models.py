from django.db import models
from django.contrib.auth.models import Group


class Batch(models.Model):
    group = models.OneToOneField(Group, related_name='batch_details', on_delete=models.CASCADE, verbose_name='batch')
    start_date = models.DateField()

    class Meta:
        permissions = (
            ('access_workshops', 'Allow User to see Workshops'),
        )
