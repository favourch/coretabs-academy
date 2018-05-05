from django.db import models
from django.utils.translation import ugettext_lazy as _
from library.utils import get_unique_slug
from django.contrib.auth.models import User


class Lesson(models.Model):
    YT_VIDEO = 'YT_VIDEO'
    MARKDOWN = 'MARKDOWN'
    QUIZ = 'QUIZ'

    TYPE_CHOICES = (
        (YT_VIDEO, 'yt-video'),
        (MARKDOWN, 'markdown'),
        (QUIZ, 'quiz'),
    )

    title = models.CharField(max_length=60, verbose_name=_('Title'))
    slug = models.SlugField(max_length=140, unique=True,
                            blank=True, allow_unicode=True, verbose_name=_('Slug'))
    type = models.CharField(
        max_length=10, choices=TYPE_CHOICES, default=MARKDOWN, verbose_name=_('Type'))
    is_shown = models.BooleanField(default=False, verbose_name=_('Is Shown'))
    url = models.URLField(verbose_name=_('URL'))
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name=_('User'))

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save()

    def __str__(self):
        return f'{self.title}'


class Module(models.Model):
    title = models.CharField(max_length=60, verbose_name=_('Title'))
    slug = models.SlugField(max_length=140, unique=True,
                            blank=True, allow_unicode=True, verbose_name=_('Slug'))
    lessons = models.ManyToManyField(
        Lesson, through='ModuleLesson', related_name='modules', verbose_name=_('Lessons'))

    class Meta:
        verbose_name = _('Module')
        verbose_name_plural = _('Modules')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save()

    def __str__(self):
        return f'{self.title}'


class ModuleLesson(models.Model):
    lesson = models.ForeignKey(
        Lesson, on_delete=models.DO_NOTHING, verbose_name=_('Lesson'))
    module = models.ForeignKey(
        Module, on_delete=models.DO_NOTHING, verbose_name=_('Module'))
    order = models.IntegerField(verbose_name=_('Order'))

    class Meta:
        verbose_name = _('Module and Lesson')
        verbose_name_plural = _('Modules and Lessons')


class Workshop(models.Model):
    BEGINNER = '0'
    INTERMEDIATE = '1'
    ADVANCED = '2'

    LEVEL_CHOICES = (
        (BEGINNER, 'beginner'),
        (INTERMEDIATE, 'intermediate'),
        (ADVANCED, 'advanced'),
    )

    title = models.CharField(max_length=60, verbose_name=_('Title'))
    slug = models.SlugField(max_length=140, unique=True,
                            blank=True, allow_unicode=True, verbose_name=_('Slug'))
    pub_date = models.DateTimeField(
        auto_now=True, verbose_name=_('Publication Date'))
    level = models.CharField(
        max_length=10, choices=LEVEL_CHOICES, default=BEGINNER, verbose_name=_('Type'))
    modules = models.ManyToManyField(
        Module, through='WorkshopModule', related_name='workshops', verbose_name=_('Modules'))

    class Meta:
        verbose_name = _('Workshop')
        verbose_name_plural = _('Workshops')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save()

    def __str__(self):
        return f'{self.title}'


class WorkshopModule(models.Model):
    module = models.ForeignKey(
        Module, on_delete=models.DO_NOTHING, verbose_name=_('Module'))
    workshop = models.ForeignKey(
        Workshop, on_delete=models.DO_NOTHING, verbose_name=_('Workshop'))
    order = models.IntegerField(verbose_name=_('Order'))

    class Meta:
        verbose_name = _('Workshop and Module')
        verbose_name_plural = _('Workshops and Modules')


class Track(models.Model):
    title = models.CharField(max_length=60, verbose_name=_('Title'))
    slug = models.SlugField(max_length=140, unique=True,
                            blank=True, allow_unicode=True, verbose_name=_('Slug'))
    workshops = models.ManyToManyField(
        Workshop, through='TrackWorkshop', related_name='tracks', verbose_name=_('Workshops'))

    class Meta:
        verbose_name = _('Track')
        verbose_name_plural = _('Tracks')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save()

    def __str__(self):
        return f'{self.title}'


class TrackWorkshop(models.Model):
    workshop = models.ForeignKey(
        Workshop, on_delete=models.DO_NOTHING, verbose_name=_('Workshop'))
    track = models.ForeignKey(
        Track, on_delete=models.DO_NOTHING, verbose_name=_('Track'))
    order = models.IntegerField(verbose_name=_('Order'))

    class Meta:
        verbose_name = _('Track and Workshop')
        verbose_name_plural = _('Tracks and Workshops')
