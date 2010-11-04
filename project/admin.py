# -*- coding: utf-8 -*-
from django.contrib import admin
from loghouse.project.models import Score, Category, Project

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('reply',)
    
admin.site.register(Score, ScoreAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
admin.site.register(Category, CategoryAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
admin.site.register(Project, ProjectAdmin)