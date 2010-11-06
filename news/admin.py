# -*- coding: utf-8 -*-
from django.contrib import admin
from loghouse.news.models import News

class NewsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Новость', {
            'classes': ['wide', 'extrapretty'],
            'fields': ('title', 'content',)
        }),
        ('Дата публикации', {
            'classes': ['wide', 'extrapretty'],
            'fields': ('add_date',)
        }),
        ('Meta данные', {'fields': ['meta_title', 'meta_description', 'meta_keywords',], 'classes': ['collapse']}),
    )
admin.site.register(News, NewsAdmin)