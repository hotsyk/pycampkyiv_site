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
        lang =2

    if int(lang) == 1:
        speaker_title = u'Speakers'
        news_title = u'News'
        twitter_title = u'Twitter'
        special_title = u"Special guest"
        speak_title = u"Talk's title"
        pycamp_date=u"2010, January 30, 09:00-19:00"
        pycamp_place =u"Mazepy str, 34, Kyiv, i-klass learning center"
        pycamp_registration = u"Registration"
        pycamp_contacts = u"Contacts"
        pycamp_tag = u"Hash tag"
    elif int(lang) == 2:
        speaker_title = u'Докладчики'
        speak_title = u"Тема доклада"
        news_title = u'Новости'
        twitter_title = u'Твиттер'
        special_title = u"Специальный гость"
        pycamp_date=u"30 января 2010, 09:00-19:00"
        pycamp_place =u"Киев, ул. Мазепы 34, учебный центр i-klass"
        pycamp_registration = u"Регистрация"
        pycamp_contacts = u"Контакты"
        pycamp_tag = u"Хеш тег"
    else:
        speaker_title = u'Доповідачі'
        speak_title = u"Тема доповіді"
        news_title = u'Новини'
        twitter_title = u'Твіттер'
        special_title = u"Спеціальний гість"
        pycamp_date=u"30 січня 2010, 09:00-19:00"
        pycamp_place =u"Київ, вул. Мазепи 34, учбовий центр i-klass"
        pycamp_registration = u"Реєстрація"
        pycamp_contacts = u"Контакти"
        pycamp_tag = u"Хеш тег"

    langs = ""
    for l in LANGUAGE_CHOICES:
        if not int(lang) == l[0]:
            lang_corr = " <a href='/?lang=%d'>%s</a>" % (l[0], l[1])
            if not langs == "":
                langs += " | " + lang_corr
            else:
                langs += lang_corr

    speakers =  []
    for sp in Speaker.objects.filter(related_speaker=None).order_by('order', 'pk'):
        sp_fields = SpeakerField.objects.filter(speaker=sp, lang=int(lang)).order_by('property_name')
        try:
            presentation = Presentation.objects.filter(speakers=sp)[0]
            presentation_title = PresentationField.objects.filter(presentation=presentation, lang=int(lang),
                property_name=1)[0].value
            try:
                presentation_description = PresentationField.objects.filter(presentation=presentation, lang=int(lang),
                    property_name=2)[0].value
            except:
                presentation_description = None
            try:
                presentation_level = PresentationField.objects.filter(presentation=presentation, lang=int(lang),
                    property_name=3)[0].value
            except:
                presentation_level = None

            speakers.append((sp, sp_fields, presentation, presentation_title, presentation_description,
                                        presentation_level ))
        except:
            speakers.append((sp, sp_fields, None, None, None, None))

    news = News.objects.filter(lang=lang, active=True,  is_flash=False).order_by('-added')[:15]
    flash_news = News.objects.filter(lang=lang, active=True,  is_flash=True).order_by('-added')[:15]

    context.update({
        'header': HeaderBlock.objects.filter(lang=lang)[0],
        'langs': langs,
        'speaker_title': speaker_title,
        'speak_title': speak_title,
        'speakers': speakers,
        'news': news,
        'pycamp_date': pycamp_date,
        'pycamp_place': pycamp_place,
        'pycamp_registration': pycamp_registration,
        'pycamp_contacts': pycamp_contacts,
        'pycamp_tag': pycamp_tag,
        'news_title' : news_title,
        'twitter_title' : twitter_title,
        'special_title' : special_title,
        'flash_news': flash_news,

    })
    return render_to_response('core/appbase.html', context)

