# -*- coding: utf-8 -*-
from django.db import models

class Score(models.Model):
    reply = models.IntegerField(verbose_name = 'Ответов')
    
    class Meta:
        verbose_name_plural = 'Оценки'
        verbose_name = 'Оценка'

class Category(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Категория')
    
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        
    def __unicode__(self):
        return self.title

class Project(models.Model):
    score = models.ForeignKey(Score, verbose_name = 'Оценка')
    category = models.ForeignKey(Category, verbose_name = 'Категория')
    title = models.CharField(max_length = 150, verbose_name = 'Название')
    area = models.CharField(max_length = 150, verbose_name = 'Площадь')
    short_content = models.TextField(verbose_name = 'Краткий контент')
    content = models.TextField(verbose_name = 'Полный контент')
    meta_title = models.CharField(max_length = 400, verbose_name = 'Title')
    meta_description = models.CharField(max_length = 400, verbose_name = 'Keywords')
    meta_keywords = models.CharField(max_length = 400, verbose_name = 'Description')
    
    class Meta:
        verbose_name_plural = 'Проекты'
        verbose_name = 'Проект'
        
    def __unicode__(self):
        return self.title