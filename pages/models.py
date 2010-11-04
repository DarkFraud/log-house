# -*- coding: utf-8 -*-
from django.db import models

class Page(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Название')
    content = models.TextField(verbose_name = 'Контент')
    meta_title = models.CharField(max_length = 400, verbose_name = 'Title')
    meta_description = models.CharField(max_length = 400, verbose_name = 'Keywords')
    meta_keywords = models.CharField(max_length = 400, verbose_name = 'Description')
    
    class Meta:
        verbose_name_plural = 'Страницы'
        verbose_name = 'Страница'
    
    def __unicode__(self):
        return self.title