from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

from caching.base import CachingManager, CachingMixin

from .utils import get_unique_slug
from . import managers

User = get_user_model()


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
    is_hidden = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('created date'), null=True)
    last_update_date = models.DateTimeField(auto_now=True, verbose_name=_('last update date'),  null=True)

    class Meta:
        verbose_name = _('module')
        verbose_name_plural = _('modules')
        ordering = ['workshopmodule__order']


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
        Module, related_name='lessons', on_delete=models.CASCADE, verbose_name=_('module'))
    shown_users = models.ManyToManyField(
        User, related_name='lessons', verbose_name=_('shown users'), blank=True)
    order = models.IntegerField(verbose_name=_('Order'), default=0)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('created date'), null=True)
    last_update_date = models.DateTimeField(auto_now=True, verbose_name=_('last update date'),  null=True)
    objects = managers.BaseLessonManager()

    class Meta:
        verbose_name = _('lesson')
        verbose_name_plural = _('lessons')
        ordering = ['order']


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
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('created date'), null=True)
    last_update_date = models.DateTimeField(auto_now=True, verbose_name=_('last update date'),  null=True)
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
    is_hidden = models.BooleanField(default=False)
    objects = managers.WorkshopManager()

    class Meta:
        verbose_name = _('workshop')
        verbose_name_plural = _('workshops')
        ordering = ['trackworkshop__order', ]


class WorkshopModule(models.Model):
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, verbose_name=_('module'))
    workshop = models.ForeignKey(
        Workshop, on_delete=models.CASCADE, verbose_name=_('workshop'))
    order = models.IntegerField(verbose_name=_('Order'), default=0)

    class Meta:
        verbose_name = _('workshop and module')
        verbose_name_plural = _('workshops and modules')
        ordering = ['order']

    def __str__(self):
        return f'{self.workshop} --> {self.module}'

class Track(CachingMixin, AutoSlugModel):
    workshops = models.ManyToManyField(
        Workshop, through='TrackWorkshop', related_name='tracks', verbose_name=_('workshops'))
    objects = CachingManager()

    class Meta:
        verbose_name = _('track')
        verbose_name_plural = _('tracks')


class TrackWorkshop(models.Model):
    workshop = models.ForeignKey(
        Workshop, on_delete=models.CASCADE, verbose_name=_('workshop'))
    track = models.ForeignKey(
        Track, on_delete=models.CASCADE, verbose_name=_('track'))
    order = models.IntegerField(verbose_name=_('Order'), default=0)

    class Meta:
        verbose_name = _('track and workshop')
        verbose_name_plural = _('tracks and workshops')
        ordering = ['order']

    def __str__(self):
        return f'{self.track} --> {self.workshop}'
