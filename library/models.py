from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from library.utils import get_unique_slug


from . import managers

from caching.base import CachingManager, CachingMixin


class AutoSlugModel(models.Model):
    title = models.CharField(max_length=60, verbose_name=_('title'))
    slug = models.SlugField(max_length=140, unique=True,
                            blank=True, allow_unicode=True, verbose_name=_('slug'))

    def save(self, *args, **kwargs):
        self.create_slug()
        super().save()

    def create_slug(self):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')

    def __str__(self):
        return f'{self.title}'

    class Meta():
        abstract = True


class Module(CachingMixin, AutoSlugModel):
    objects = CachingManager()

    class Meta:
        verbose_name = _('module')
        verbose_name_plural = _('modules')


class BaseLesson(CachingMixin, AutoSlugModel):
    YOUTUBE_VIDEO = '0'
    SCRIMBA_VIDEO = '1'
    MARKDOWN = '2'
    QUIZ = '3'
    TASK = '4'

    TYPE_CHOICES = (
        (YOUTUBE_VIDEO, 'youtube-video'),
        (SCRIMBA_VIDEO, 'scrimba-video'),
        (MARKDOWN, 'markdown'),
        (QUIZ, 'quiz'),
        (TASK, 'task'),
    )

    type = models.CharField(
        max_length=10, choices=TYPE_CHOICES, default=MARKDOWN, verbose_name=_('type'))

    module = models.ForeignKey(
        Module, related_name='lessons', on_delete=models.DO_NOTHING, verbose_name=_('module'))
    shown_users = models.ManyToManyField(
        User, related_name='lessons', verbose_name=_('shown users'), blank=True)
    order = models.IntegerField(verbose_name=_('Order'), default=0)

    objects = managers.BaseLessonManager()

    class Meta:
        verbose_name = _('lesson')
        verbose_name_plural = _('lessons')


class MarkdownLesson(BaseLesson):
    markdown_url = models.URLField(verbose_name=_('markdown url'))


class QuizLesson(BaseLesson):
    markdown_url = models.URLField(verbose_name=_('markdown url'))


class VideoLesson(BaseLesson):
    video_url = models.URLField(verbose_name=_('video url'))
    markdown_url = models.URLField(verbose_name=_('markdown url'))


class Workshop(CachingMixin, AutoSlugModel):
    BEGINNER = '0'
    INTERMEDIATE = '1'
    ADVANCED = '2'

    LEVEL_CHOICES = (
        (BEGINNER, 'beginner'),
        (INTERMEDIATE, 'intermediate'),
        (ADVANCED, 'advanced'),
    )

    level = models.CharField(
        max_length=10, choices=LEVEL_CHOICES, default=BEGINNER, verbose_name=_('type'))
    last_update_date = models.DateTimeField(
        auto_now=True, verbose_name=_('last update date'))
    duration = models.DecimalField(
        max_digits=3, decimal_places=1, verbose_name=_('duration'))
    description = models.CharField(
        max_length=1000, blank=True, verbose_name=_('description'))
    used_technologies = models.CharField(
        max_length=100, blank=True, verbose_name=_('used technologies'))
    workshop_result_url = models.URLField(
        verbose_name=_('workshop result url'))
    workshop_forums_url = models.URLField(
        verbose_name=_('workshop forum url'))
    authors = models.ManyToManyField(
        User, related_name='workshops', verbose_name=_('authors'))
    modules = models.ManyToManyField(
        Module, through='WorkshopModule', related_name='workshops', verbose_name=_('modules'))

    objects = managers.WorkshopManager()

    def shown_percentage(self, user, workshop):
        return Workshop.objects.shown_percentage(user=user, workshop=workshop)

    class Meta:
        verbose_name = _('workshop')
        verbose_name_plural = _('workshops')


class WorkshopModule(models.Model):
    module = models.ForeignKey(
        Module, on_delete=models.DO_NOTHING, verbose_name=_('module'))
    workshop = models.ForeignKey(
        Workshop, on_delete=models.DO_NOTHING, verbose_name=_('workshop'))
    order = models.IntegerField(verbose_name=_('Order'), default=0)

    class Meta:
        verbose_name = _('workshop and module')
        verbose_name_plural = _('workshops and modules')
        ordering = ['order', ]


class Track(CachingMixin, AutoSlugModel):
    workshops = models.ManyToManyField(
        Workshop, through='TrackWorkshop', related_name='tracks', verbose_name=_('workshops'))
    objects = CachingManager()

    class Meta:
        verbose_name = _('track')
        verbose_name_plural = _('tracks')


class TrackWorkshop(models.Model):
    workshop = models.ForeignKey(
        Workshop, on_delete=models.DO_NOTHING, verbose_name=_('workshop'))
    track = models.ForeignKey(
        Track, on_delete=models.DO_NOTHING, verbose_name=_('track'))
    order = models.IntegerField(verbose_name=_('Order'), default=0)

    class Meta:
        verbose_name = _('track and workshop')
        verbose_name_plural = _('tracks and workshops')
        ordering = ['order', ]


class Profile(models.Model):
    # S means Student
    role = models.CharField(max_length=1000, blank=True,
                            default='S', verbose_name=_('role'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    track = models.ForeignKey(
        Track, on_delete=models.DO_NOTHING, verbose_name=_('track'), null=True)
    last_opened_lesson = models.OneToOneField(BaseLesson,
                                              on_delete=models.DO_NOTHING,
                                              verbose_name=_('last opened lesson'), null=True)

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')


"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, name=instance.first_name)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""
