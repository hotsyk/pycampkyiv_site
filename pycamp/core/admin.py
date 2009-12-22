# -*- coding: utf-8

from django.contrib import admin
from models import *

class SpeakerFieldsInlines(admin.TabularInline):
    model = SpeakerField


class SpeakerAdmin(admin.ModelAdmin):
        inlines = [
        SpeakerFieldsInlines,
    ]


admin.site.register(Speaker, SpeakerAdmin)

class PresentationFieldInlines(admin.TabularInline):
    model = PresentationField


class PresentationAdmin(admin.ModelAdmin):
        inlines = [
        PresentationFieldInlines,
    ]


admin.site.register(Presentation, PresentationAdmin)

class HeaderAdmin(admin.ModelAdmin):
    pass


admin.site.register(HeaderBlock, HeaderAdmin)

