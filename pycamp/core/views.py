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
        pycamp_registration2=u"Registration is closed"
        converence_over =u"Conference is over. Stay tuned for the video and slides"
        schedule = u"""
<tr>
   <td > 09:00</td><td>09:45</td><td colspan="2">Registration</td>
</tr>
<tr>
    <td>09:45</td><td>10:10</td><td colspan="2">Introduction</td>
</tr>
<tr>
    <td>10:10</td><td>10:50</td><td>Why Python is the brake and how to make it little more faster.</td><td>   Alexander Shigin</td>
</tr>
<tr>
    <td>10:50</td><td>11:30</td><td>Decorators' recipes </td><td>Yury Yurevich</td>
</tr>
<tr>
    <td>11:30</td><td>11:50</td><td colspan="2">Coffee break</td>
</tr>
<tr>
    <td>11:50</td><td>12:10</td><td>Programming on the nerves</td><td>Dmitry Kozhevin</td>
</tr>
<tr>
    <td>12:10</td><td>12:50</td><td>Working with the Google App Engine datastore, differences from the relational model.</td><td> Mikhail Kashkin</td>
</tr>
<tr>
    <td>12:50</td><td>13:20</td><td> Redis: Wild West of databases </td><td>Alexander Solovyov</td>
</tr>
<tr>
    <td>13:20</td><td>14:45</td><td colspan="2">Lunch</td>
</tr>
<tr>
    <td>14:45</td><td>15:30</td><td>Safe software development as a result of the long way and many bumps filled. </td><td>Andrew Svetlov</td>
</tr>
<tr>
    <td>15:30</td><td>16:10</td><td>Python: Extending and Embedding</td><td>Vladimir Pouzanov, Vladimir Kirillov</td>
</tr>
<tr>
    <td>16:10</td><td>16:20</td><td colspan="2">Coffee break</td>
</tr>
<tr>
    <td>16:20</td><td>16:50</td><td> Using Python in GIS </td><td>Andrii Mishkovskyi</td>
</tr>
<tr>
    <td>16:50</td><td>17:20</td><td>WebSockets in Twisted </td><td>Sergey Kirillov</td>
</tr>
<tr>
    <td>17:20</td><td>17:30</td><td colspan="2"> Coffee break</td>
</tr>
<tr>
    <td>17:30</td><td>18:00</td><td>Internationalization and localization of the Python-applications with the gettext.</td><td>Alexander Belchenko</td>
</tr>
<tr>
    <td>18:00</td><td>18:30</td><td> Working with the payment systems in Django (PayPal, WebMoney).</td><td> Ivan Morgun</td>
</tr>
<tr>
    <td>18:30</td><td>18:50</td><td>PyCharm – new python IDE from JetBrains</td><td> Dmitry Jemerov</td>
</tr>
         """
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
        pycamp_registration2=u"Регистрация закрыта"
        converence_over =u"Конференция завершена. Ждите видео"
        schedule = u"""
<tr>
   <td > 09:00</td><td>09:45</td><td colspan="2">Регистрация</td>
</tr>
<tr>
    <td>09:45</td><td>10:10</td><td colspan="2">Вступительное слово</td>
</tr>
<tr>
    <td>10:10</td><td>10:50</td><td>Почему Python - тормоз и как заставить его меньше тормозить.</td><td>   Александр Шигин</td>
</tr>
<tr>
    <td>10:50</td><td>11:30</td><td>Рецепты декораторов</td><td>Юрий Юревич</td>
</tr>
<tr>
    <td>11:30</td><td>11:50</td><td colspan="2">Кофе-брейк</td>
</tr>
<tr>
    <td>11:50</td><td>12:10</td><td>Программирование на нервах</td><td>Дмитрий Кожевин</td>
</tr>
<tr>
    <td>12:10</td><td>12:50</td><td>Работа с хранилищем данных в Google App Engine, отличия от реляционной модели.</td><td> Михаил Кашкин</td>
</tr>
<tr>
    <td>12:50</td><td>13:20</td><td>    Redis: Дикий Запад баз данных   </td><td>Александр Соловьев</td>
</tr>
<tr>
    <td>13:20</td><td>14:45</td><td colspan="2">Обед</td>
</tr>
<tr>
    <td>14:45</td><td>15:30</td><td> Безопасная разработка ПО. Результат длинного пути и множества набитых шишек. </td><td>   Андрей Светлов</td>
</tr>
<tr>
    <td>15:30</td><td>16:10</td><td>Расширение и встраивание Python</td><td> Владимир Пузанов, Владимир Кириллов</td>
</tr>
<tr>
    <td>16:10</td><td>16:20</td><td colspan="2">Кофе-брейк  </td>
</tr>
<tr>
    <td>16:20</td><td>16:50</td><td> Использование Python в ГИС </td><td> Андрей Мишковский</td>
</tr>
<tr>
    <td>16:50</td><td>17:20</td><td>WebSockets в Twisted  </td><td>  Сергей Кириллов</td>
</tr>
<tr>
    <td>17:20</td><td>17:30</td><td colspan="2"> Кофе-брейк  </td>
</tr>
<tr>
    <td>17:30</td><td>18:00</td><td>Интернационализация и локализация Python-приложений с использованием gettext.  </td><td> Александр Бельченко</td>
</tr>
<tr>
    <td>18:00</td><td>18:30</td><td> Работа с платежными системами в Django (PayPal, WebMoney). </td><td> Иван Моргун</td>
</tr>
<tr>
    <td>18:30</td><td>18:50</td><td>PyCharm – новая python IDE от JetBrains </td><td> Дмитрий Жемеров</td>
</tr>
         """
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
        pycamp_registration2=u"Реєстрацію припинено"
        converence_over =u"Конференцію завершено. Очікуйте на відео"
        schedule = u"""
<tr>
   <td > 09:00</td><td>09:45</td><td colspan="2">Реєстрація</td>
</tr>
<tr>
    <td>09:45</td><td>10:10</td><td colspan="2">Вітальне слово</td>
</tr>
<tr>
    <td>10:10</td><td>10:50</td><td>Чому Python - гальмо і як змусити його гальмувати менше</td><td> Олександр Шигін</td>
</tr>
<tr>
    <td>10:50</td><td>11:30</td><td>Рецепти декораторів</td><td>Юрій Юревіч</td>
</tr>
<tr>
    <td>11:30</td><td>11:50</td><td colspan="2">Кофе-брейк</td>
</tr>
<tr>
    <td>11:50</td><td>12:10</td><td>Програмування на нервах</td><td>Дмитро Кожевін</td>
</tr>
<tr>
    <td>12:10</td><td>12:50</td><td>Робота зі сховищем даних в Google App Engine, відмінності від реляційної моделі</td><td>Михайло Кашкін</td>
</tr>
<tr>
    <td>12:50</td><td>13:20</td><td>   Redis: Дикий Захід баз даних  </td><td>Олександр Соловйов</td>
</tr>
<tr>
    <td>13:20</td><td>14:45</td><td colspan="2">Обід</td>
</tr>
<tr>
    <td>14:45</td><td>15:30</td><td>Безпечна розробка ПЗ. Результат довгого шляху та величезної кількості набитих гуль.</td><td> Андрій Светлов</td>
</tr>
<tr>
    <td>15:30</td><td>16:10</td><td>Розширення та вбудовування Python</td><td>Володимир Пузанов, Володимир Кирилов</td>
</tr>
<tr>
    <td>16:10</td><td>16:20</td><td colspan="2">Кофе-брейк  </td>
</tr>
<tr>
    <td>16:20</td><td>16:50</td><td> Використання Python в ГІС </td><td> Андрій Мішковський</td>
</tr>
<tr>
    <td>16:50</td><td>17:20</td><td>WebSockets в Twisted</td><td> Сергій Кіріллов</td>
</tr>
<tr>
    <td>17:20</td><td>17:30</td><td colspan="2"> Кофе-брейк  </td>
</tr>
<tr>
    <td>17:30</td><td>18:00</td><td>Інтернаціоналізація та локалізація Python-застосувань з використанням gettext.</td><td> Олександр Бєльченко</td>
</tr>
<tr>
    <td>18:00</td><td>18:30</td><td>Робота з платіжними системами в Django (PayPal, WebMoney).</td><td> Іван Моргун</td>
</tr>
<tr>
    <td>18:30</td><td>18:50</td><td>PyCharm – нова python IDE від JetBrains </td><td> Дмитро Жемеров</td>
</tr>
         """
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

    video = LiveSettings.objects.filter(title='video')
    if len(video) > 0:
        video = video[0].is_active
    else:
        video = False

    context.update({
        'langs': langs,
        'speakers': speakers,
        'news': news,
        'flash_news': flash_news,
        'pycamp_registration2': pycamp_registration2,
        'schedule': schedule,
        'video': video,
        'converence_over':converence_over, 
               'presentations': Presentation.objects.all()
    })
    return render_to_response('core/main-post.html', context)

def live_video(request):

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
        pycamp_registration2=u"Registration is closed"

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
        pycamp_registration2=u"Регистрация закрыта"

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
        pycamp_registration2=u"Реєстрацію припинено"

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

    video = LiveSettings.objects.filter(title='video')
    if len(video) > 0:
        video = video[0].is_active
    else:
        video = False

    context.update({
        'header': HeaderBlock.objects.filter(lang=lang)[0],
        'langs': langs,
        'speaker_title': speaker_title,
        'speak_title': speak_title,
        'speakers': speakers,

        'pycamp_date': pycamp_date,
        'pycamp_place': pycamp_place,
        'pycamp_registration': pycamp_registration,
        'pycamp_contacts': pycamp_contacts,
        'pycamp_tag': pycamp_tag,
        'news_title' : news_title,
        'twitter_title' : twitter_title,
        'special_title' : special_title,
        'pycamp_registration2': pycamp_registration2,
        'video': video, 
  
    })
    if video:
        return render_to_response('core/video.html', context)
    else:
        return main_page(request)


def presentation(request,  id=0):

    context = RequestContext(request)
    if request.method == 'GET':
        lang = request.GET.get('lang', None)
    speaker_title = ''

    if lang is None:
        lang =2

   
    langs = ""
    for l in LANGUAGE_CHOICES:
        if not int(lang) == l[0]:
            lang_corr = " <a href='/?lang=%d'>%s</a>" % (l[0], l[1])
            if not langs == "":
                langs += " | " + lang_corr
            else:
                langs += lang_corr

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

    context.update({
        'speaker': speaker,
    })
    return render_to_response('core/presentation.html', context)
