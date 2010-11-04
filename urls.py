# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin_tools/', include('admin_tools.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_TIMY_ROOT, 'show_indexes': True}),
)
