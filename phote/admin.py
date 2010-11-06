# -*- coding: utf-8 -*-
from django.contrib import admin
from loghouse.phote.models import Picture, Album, OtherAlbum

class PictureAdmin(admin.ModelAdmin):
    class Media:
        js = [
            'javascript/admin/display_thumbs.js',
            'javascript/admin/tiny_django_browser.js',
            ]
    list_display = ['description', 'get_thumbnail_html']

admin.site.register(Picture, PictureAdmin)

class AlbumAdmin(admin.ModelAdmin):
    class Media:
        js = ['javascript/admin/display_thumbs.js',]
    list_display = ['project', 'get_thumbnail_html',]
    
admin.site.register(Album, AlbumAdmin)

class OtherAlbumAdmin(admin.ModelAdmin):
    class Media:
        js = ['javascript/admin/display_thumbs.js',]
    list_display = ['title', 'get_thumbnail_html']
    
admin.site.register(OtherAlbum, OtherAlbumAdmin)