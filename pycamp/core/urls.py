from django.conf.urls.defaults import *

urlpatterns = patterns('pycamp.core.views',
       url(r'^$', 'view1', name='view1'),
       )
