from django.conf.urls import patterns, include, url
from django.contrib import admin

import myapp.views

urlpatterns = patterns(
    '',
    url(r'^$',  myapp.views.index, name='index'),
    url(r'^produce/', myapp.views.produce, name='produce'),
    url(r'^consume/', myapp.views.consume, name='consume'),
    url(r'^admin/', include(admin.site.urls)),
)
