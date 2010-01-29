# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

__all__ = ('Speaker',  'SpeakerField', 'Presentation', 'PresentationField', 'HeaderBlock',
    'LANGUAGE_CHOICES', 'News', 'LiveSettings')

class Speaker (models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    email = models.EmailField(_('Email'),)
    site = models.URLField(_('Site'), blank=True, null=True)
    blog = models.URLField(_('Blog'), blank=True, null=True)
    twitter_name = models.CharField(_('Speaker twitter'), max_length=255, blank=True, null=True)
    photo = models.ImageField(_('Photo'), upload_to=".", blank=True, null=True)
    related_speaker = models.ForeignKey('Speaker', blank=True, null=True)
    order = models.IntegerField(_("Speaker's order"), default=100)
    special = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return ""

    get_absolute_url = permalink(get_absolute_url)

LANGUAGE_CHOICES = (
    (1, u'english'),
    (2, u'русский'),
    (3, u'українська'),
    )


PROPERTY_CHOICES = (
    (1, u'Name'),
    (2, u'Location'),
    (3, u'Company'),
    (4, u'Position'),
    (5, u'Bio'),
    )

class SpeakerField(models.Model):
    speaker = models.ForeignKey(Speaker)
    lang = models.SmallIntegerField(_('Language'), choices=LANGUAGE_CHOICES, )
    property_name = models.SmallIntegerField(_('Property'), choices=PROPERTY_CHOICES, )
    value = models.TextField(_('Value'), blank=True, null=True)

    def __unicode__(self):
        return "%s (%s, %s)" % (self.speaker, self.lang, self.property_name)

    #class Meta:
     #   unique_together = ("speaker", "lang", "property_name")


class Presentation(models.Model):
    speakers = models.ForeignKey(Speaker, blank=True, null=True)
    time_start = models.TimeField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)
    file = models.FileField(_('Presentation file'), upload_to='.', blank=True, null=True)

    def __unicode__(self):
       return unicode(self.pk)

    def get_absolute_url(self):
        return ""

    get_absolute_url = permalink(get_absolute_url)

PRESENTATION_CHOICES = (
    (1, u'Title'),
    (2, u'Description'),
    (3, u'Listeners level'),
    )

class PresentationField(models.Model):
    presentation = models.ForeignKey(Presentation)
    lang = models.SmallIntegerField(_('Language'), choices=LANGUAGE_CHOICES, )
    property_name = models.SmallIntegerField(_('Property'), choices=PRESENTATION_CHOICES, )
    value = models.TextField(_('Value'), blank=True, null=True)


class HeaderBlock (models.Model):
    lang = models.SmallIntegerField(_('Language'), choices=LANGUAGE_CHOICES, unique=True )
    text = models.TextField(_('Raw text'), blank=True, null=True)

    def __unicode__(self):
        for l in LANGUAGE_CHOICES:
            if self.lang == l[0]:
                return l[1]


class News(models.Model):
    lang = models.SmallIntegerField(_('Language'), choices=LANGUAGE_CHOICES)
    title = models.CharField(max_length=255)
    text = models.TextField(_('Value'), blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    is_flash = models.BooleanField(default=False)

class LiveSettings(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
