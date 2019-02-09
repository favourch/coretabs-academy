import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from django.dispatch import receiver

User = get_user_model()


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # More info

    def __str__(self):
        return self.name


class Profile(models.Model):
    ROLE_CHOICES = (
        ('0', _('Student')),
        ('1', _('Mentor')),
        ('2', _('Author')),
        ('3', _('Admin')),
    )
    LEVEL_CHOICES = (
        ('0', _('Beginner')),
        ('1', _('Intermediate')),
        ('2', _('Advanced')),
    )

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    # name and join date come from user

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='0')
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='0')
    description = models.CharField(max_length=50, blank=True)
    available_for_work = models.BooleanField(default=False, verbose_name='available for work')
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    bio = models.CharField(max_length=1000, blank=True)
    skills = models.CharField(max_length=100, blank=True)
    preferred_skills = models.CharField(max_length=100, blank=True)
    languages = models.CharField(max_length=100, blank=True)
    team = models.ForeignKey(Team, blank=True, null=True,
                             related_name='members', on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.user.first_name} ({self.user.username})'


class SocialLink(models.Model):
    APP_CHOICES = (
        ('0', _('Facebook')),
        ('1', _('Twitter')),
        ('2', _('LinkedIn')),
        ('3', _('Google')),
        ('4', _('Personal website'))
    )

    profile = models.ForeignKey(Profile, related_name='social_links', on_delete=models.CASCADE)
    social_app = models.CharField(max_length=10, choices=APP_CHOICES)
    link = models.URLField()

    def __str__(self):
        return f'{self.profile.user.username} ({self.link})'


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
