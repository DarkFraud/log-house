# -*- coding: utf-8 -*-
from django.contrib import admin
from loghouse.article.models import Article

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Статья', {
            'classes': ['wide', 'extrapretty'],
            'fields': ('title', 'content',)
        }),
        ('Meta данные', {'fields': ['meta_title', 'meta_description', 'meta_keywords',], 'classes': ['collapse']}),
    )
admin.site.register(Article, ArticleAdmin)