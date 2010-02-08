from django.conf.urls.defaults import *

urlpatterns = patterns('pycamp.core.views',
       url(r'^$', 'main_page', name='main_page'),
       #url(r'^live/$', 'live_video', name='live_video'),
       url(r'^presentation/(?P<id>\d+)$', 'presentation', name='presentation'),
       url(r'^videos/$', 'videos', name='videos'),
       url(r'^presentations/$', 'presentations', name='presentations'),
       )
