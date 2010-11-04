# -*- coding: utf-8 -*-
from django.contrib import admin
from loghouse.project.models import Score, Category, Project

admin.site.register(Score)
admin.site.register(Category)

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Продукт', {
            'classes': ['wide', 'extrapretty'],
            'fields': ('category', 'title', 'area', 'short_content', 'content', 'score',)
        }),
        ('Meta данные', {'fields': ['meta_title', 'meta_description', 'meta_keywords',], 'classes': ['collapse']}),
    )
admin.site.register(Project, ProjectAdmin)