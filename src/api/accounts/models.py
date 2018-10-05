from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()


class Batch(models.Model):
    group = models.OneToOneField(Group, related_name='batch_details',
                                 null=True, blank=True, on_delete=models.CASCADE,
                                 verbose_name='group (Added Automatically)')
    name = models.CharField(max_length=20)
    users_number = models.PositiveIntegerField(verbose_name='users number')
    start_date = models.DateField()

    class Meta:
        permissions = (
            ('access_workshops', 'Allow User to see Workshops'),
        )
        verbose_name = 'batch'
        verbose_name_plural = 'batches'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.group:
            group = Group.objects.create(name=self.name)
            self.group = group

        self.prepare_batch()
        super().save()

    def prepare_batch(self):
        batch_group = self.group
        users = User.objects.all().order_by('date_joined')
        limit = self.users_number

        with transaction.atomic():
            for user in users:
                if limit < 1:
                    break
                if user.groups.all():
                    continue

                user.groups.add(batch_group)
                limit -= 1

        final_users_number = self.users_number - limit
        self.users_number = final_users_number

    def __str__(self):
        return self.name

