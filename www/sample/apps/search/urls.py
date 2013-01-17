# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'apps.search.views',
    url(r'^$', 'search', name='search'),
)
