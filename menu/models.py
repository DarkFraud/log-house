# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length  = 150, verbose_name = 'Название')
    
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
    
    def __unicode__(self):
        return self.title

class Menu(models.Model):
    parent = models.ForeignKey('self', blank = True, null = True, verbose_name = 'Родитель')
    title = models.CharField(max_length = 150, verbose_name = 'Название')
    url = models.CharField(max_length = 400, verbose_name = 'URL адрес')
    
    class Meta:
        verbose_name_plural = 'Меню'
        verbose_name = 'Меню'
    
    def __unicode__(self):
        return self.title