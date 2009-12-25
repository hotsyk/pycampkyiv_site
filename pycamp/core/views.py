# -*- coding:utf-8 -*
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from pycamp.core.models import *

def main_page(request):

    context = RequestContext(request)
    if request.method == 'GET':
        lang = request.GET.get('lang', None)
    speaker_title = ''

    if lang is None:
        if request.LANGUAGE_CODE == 'en':
            lang = 1
        elif request.LANGUAGE_CODE == 'ru':
            lang = 2
        elif request.LANGUAGE_CODE == 'uk':
            lang = 3
        else:
            lang =2

    if int(lang) == 1:
        speaker_title = u'Speakers'
        speak_title = u"Talk's title"
    elif int(lang) == 2:
        speaker_title = u'Докладчики'
        speak_title = u"Тема доклада"
    else:
        speaker_title = u'Доповідачі'
        speak_title = u"Тема доповіді"

    langs = ""
    for l in LANGUAGE_CHOICES:
        if not int(lang) == l[0]:
            lang_corr = " <a href='/?lang=%d'>%s</a>" % (l[0], l[1])
            if not langs == "":
                langs += " | " + lang_corr
            else:
                langs += lang_corr

    speakers =  []
    for sp in Speaker.objects.filter(related_speaker=None):
        sp_fields = SpeakerField.objects.filter(speaker=sp, lang=int(lang)).order_by('property_name')
        try:
            presentation = Presentation.objects.filter(speakers=sp)[0]
            presentation_title = PresentationField.objects.filter(presentation=presentation, lang=int(lang),
                property_name=1)[0].value
            speakers.append((sp, sp_fields, presentation, presentation_title ))
        except:
            speakers.append((sp, sp_fields, None, None))


    context.update({
        'header': HeaderBlock.objects.filter(lang=lang)[0],
        'langs': langs,
        'speaker_title': speaker_title,
        'speak_title': speak_title,
        'speakers': speakers,

    })
    return render_to_response('core/appbase.html', context)

