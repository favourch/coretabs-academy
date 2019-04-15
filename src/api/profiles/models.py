import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from django.dispatch import receiver

User = get_user_model()


class Profile(models.Model):
    ROLE_CHOICES = (
        ('0', _('Student')),
        ('1', _('Mentor')),
        ('2', _('Tutor')),
        ('3', _('Admin')),
    )
    LEVEL_CHOICES = (
        ('0', _('Beginner')),
        ('1', _('Intermediate')),
        ('2', _('Advanced')),
    )
    COUNTRY_CHOICES = (
        ('', ''),
        ('DZ', _('Algeria')),
        ('TN', _('Tunisia')),
    )
    LANGUAGES_CHOICES = [('ar', 'العربية'), ('fr', 'Français'), ('en', 'English'), ('es', 'español')]

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='0')
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='0')
    description = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True, choices=COUNTRY_CHOICES)
    bio = models.CharField(max_length=1000, blank=True)
    languages = models.CharField(max_length=100, blank=True)
    facebook_link = models.CharField(max_length=100, blank=True)
    twitter_link = models.CharField(max_length=100, blank=True)
    linkedin_link = models.CharField(max_length=100, blank=True)
    website_link = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.first_name} ({self.user.username})'


class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='certificates')
    full_name = models.CharField(max_length=126, verbose_name='full name')
    date = models.DateField(auto_now=True)
    template = models.ForeignKey('CertificateTemplate', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.template}: {self.full_name}'


class CertificateTemplate(models.Model):
    heading = models.CharField(max_length=126)
    body = models.CharField(max_length=512)
    signature = models.ForeignKey('CertificateSignature', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.heading


class CertificateSignature(models.Model):
    name = models.CharField(max_length=126)
    photo = models.ImageField(upload_to='signatures/')

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
