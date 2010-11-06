# -*- coding: utf-8 -*-
from django.contrib import admin
from loghouse.images.models import Image

class ImageAdmin(admin.ModelAdmin):
    class Media:
        js = [
            'javascript/admin/tiny_django_browser.js',
            'javascript/admin/display_thumbs.js',
            ]
    list_display = ['title', 'get_thumbnail_html']
    
admin.site.register(Image, ImageAdmin)