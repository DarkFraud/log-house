# -*- coding: utf-8 -*-
from django.contrib import admin
from loghouse.pages.models import Page

class PageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Страница', {
            'classes': ['wide', 'extrapretty'],
            'fields': ('title', 'content',)
        }),
        ('Meta данные', {'fields': ['meta_title', 'meta_description', 'meta_keywords',], 'classes': ['collapse']}),
    )
admin.site.register(Page, PageAdmin)