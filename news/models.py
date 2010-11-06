# -*- coding: utf-8 -*-
from django.db import models
import datetime

class News(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Название')
    content = models.TextField(verbose_name = 'Контент')
    add_date = models.DateTimeField(default=datetime.datetime.now, verbose_name = 'Дата')
    meta_title = models.CharField(max_length = 400, verbose_name = 'Title')
    meta_description = models.CharField(max_length = 400, verbose_name = 'Keywords')
    meta_keywords = models.CharField(max_length = 400, verbose_name = 'Description')
    
    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
        
    def __unicode__(self):
        return self.title