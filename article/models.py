# -*- coding: utf-8 -*-
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Название')
    content = models.TextField(verbose_name = 'Контент')
    
    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статья'
    
    def __unicode__(self):
        return self.title