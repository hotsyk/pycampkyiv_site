# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

__all__ = ('Speaker',  'SpeakerField', 'Presentation', 'PresentationField', 'HeaderBlock',
    'LANGUAGE_CHOICES')


class Speaker (models.Model):
    user = models.ForeignKey(User)
    email = models.EmailField()
    site = models.URLField(blank=True, null=True)

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
    (1, u'Bio'),
    (2, u'Location'),
    (3, u'Name'),
    )

class SpeakerField(models.Model):
    speaker = models.ForeignKey(Speaker)
    lang = models.SmallIntegerField(_('Language'), choices=LANGUAGE_CHOICES, )
    property_name = models.SmallIntegerField(_('Property'), choices=PROPERTY_CHOICES, )
    value = models.TextField(_('Value'), blank=True, null=True)

    def __unicode__(self):
        return "%s (%s, %s)" % (self.speaker, self.lang, self.property)

    class Meta:
        unique_together = ("speaker", "lang", "property_name")


class Presentation(models.Model):
    speakers = models.ManyToManyField(Speaker)
    time_start = models.TimeField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)
    file = models.FileField(upload_to='.', blank=True, null=True)

    #def __unicode__(self):
    #   return self.pk

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

    #def __unicode__(self):
     #   return self.lang


