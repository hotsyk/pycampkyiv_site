# -*- coding:utf-8 -*
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from pycamp.core.models import *

LANGUAGE_CHOICES = (
    ('en', u'english',  1),
    ('ru-ru', u'русский',  2),
    ('uk-ua', u'українська',  3),
    )

def intern(lang):
    if lang==1:
            org_words = u"Words from the organizers:"
            participants_words =u"Comments from the participants:"
            video_menu = u"Video from the conference"
            presentation_menu = u"Presentations from the conference"
    elif lang==2:
            org_words = u"Несколько слов от организаторов:"
            participants_words =u"Комментарии участников:"        
            video_menu = u"Видео докладов"
            presentation_menu = u"Презентации"
    elif lang==3:
            org_words = u"Кілька слів від організаторів:"
            participants_words =u"Коментарі відвідувачів:"        
            video_menu = u"Відео доповідей"
            presentation_menu = u"Презентації"
    else:
            org_words = u"Words from the organizers:"
            participants_words =u"Comments from the participants:"        
            video_menu = u"Video from the conference"
            presentation_menu = u"Presentations from the conference"
        
    return  org_words,  participants_words,  video_menu,  presentation_menu
    
def main_page(request):
    context = RequestContext(request)
    cur_lang = request.LANGUAGE_CODE
    lang=2
    for l in LANGUAGE_CHOICES:
        if l[0] == cur_lang:
            lang = l[2]
    header = HeaderBlock.objects.filter(lang=lang)[0].text
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

    video = LiveSettings.objects.filter(title='video')
    if len(video) > 0:
        video = video[0].is_active
    else:
        video = False
    org_words,  participants_words,  video_menu,  presentation_menu = intern(lang)
    context.update({
        'speakers': speakers,
        'header': header, 
         'presentations': Presentation.objects.all(), 
         'org_words': org_words, 
         'participants_words': participants_words, 
         'video_menu': video_menu, 
         'presentation_menu': presentation_menu
    })
    return render_to_response('core/main-post.html', context)

def presentation(request,  id=0):

    context = RequestContext(request)

    cur_lang = request.LANGUAGE_CODE
    lang=2
    for l in LANGUAGE_CHOICES:
        if l[0] == cur_lang:
            lang = l[2]

    speakers =  []
    if id:
        sp = Speaker.objects.filter(pk=id)[0]
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
        
            speaker = (sp, sp_fields, presentation, presentation_title, presentation_description,
                                        presentation_level )
        except:
            speaker = (sp, sp_fields, None, None, None, None)
    else:
        return main_page(request)
    header = HeaderBlock.objects.filter(lang=lang)[0].text
    org_words,  participants_words,  video_menu,  presentation_menu = intern(lang)
    
    context.update({
        'speaker': speaker,
         'header': header, 
         'org_words': org_words, 
         'participants_words': participants_words, 
         'video_menu': video_menu, 
         'presentation_menu': presentation_menu         
    })
    return render_to_response('core/presentation.html', context)

def videos(request):

    context = RequestContext(request)

    cur_lang = request.LANGUAGE_CODE
    lang=2
    for l in LANGUAGE_CHOICES:
        if l[0] == cur_lang:
            lang = l[2]
    videos = []
    for video in Presentation.objects.exclude(embedded_video="").exclude(embedded_video=None):
        speaker_name = SpeakerField.objects.filter(speaker=video.speakers, lang=int(lang),  property_name=1)[0].value
        presentation_name = PresentationField.objects.filter(presentation=video,  lang=int(lang),  property_name=1)[0].value
        videos.append((video.embedded_video,  speaker_name,  presentation_name))

    header = HeaderBlock.objects.filter(lang=lang)[0].text
    org_words,  participants_words,  video_menu,  presentation_menu = intern(lang)
    
    context.update({
        'videos':videos, 
         'header': header, 
         'org_words': org_words, 
         'participants_words': participants_words, 
         'video_menu': video_menu, 
         'presentation_menu': presentation_menu , 
         
    })
    return render_to_response('core/videos.html', context)
    
def presentations(request):

    context = RequestContext(request)

    cur_lang = request.LANGUAGE_CODE
    lang=2
    for l in LANGUAGE_CHOICES:
        if l[0] == cur_lang:
            lang = l[2]

    presentations = []
    for presentation in Presentation.objects.exclude(embedded_pdf="").exclude(embedded_pdf=None):
        speaker_name = SpeakerField.objects.filter(speaker=presentation.speakers, lang=int(lang),  property_name=1)[0].value
        presentation_name = PresentationField.objects.filter(presentation=presentation,  lang=int(lang),  property_name=1)[0].value
        presentations.append((presentation.embedded_pdf,   speaker_name,  presentation_name))

    header = HeaderBlock.objects.filter(lang=lang)[0].text
    org_words,  participants_words,  video_menu,  presentation_menu = intern(lang)
    
    context.update({
        'presentations':presentations, 
         'header': header, 
         'org_words': org_words, 
         'participants_words': participants_words, 
         'video_menu': video_menu, 
         'presentation_menu': presentation_menu , 
         
    })
    return render_to_response('core/presentations.html', context)    
