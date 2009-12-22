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

    if lang is None:
        if request.LANGUAGE_CODE == 'en':
            lang = 1
        elif request.LANGUAGE_CODE == 'ru':
            lang = 2
        elif request.LANGUAGE_CODE == 'uk':
            lang = 3
        else:
            lang =1

    langs = ""
    for l in LANGUAGE_CHOICES:
        if not int(lang) == l[0]:
            lang_corr = " <a href='/?lang=%d'>%s</a>" % (l[0], l[1])
            if not langs == "":
                langs += " | " + lang_corr
            else:
                langs += lang_corr


    context.update({
        'header': HeaderBlock.objects.filter(lang=lang)[0],
        'langs': langs,
    })
    return render_to_response('core/appbase.html', context)

