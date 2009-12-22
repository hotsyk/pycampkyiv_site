from django.conf.urls.defaults import *

urlpatterns = patterns('pycamp.core.views',
       url(r'^$', 'main_page', name='main_page'),
       )
