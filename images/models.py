# -*- coding: utf-8 -*-
from django.db import models

class Image(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Название')
    file = models.ImageField(upload_to = 'Images/', verbose_name = 'Изображение')
    
    class Meta:
        verbose_name_plural = 'Изображения'
        verbose_name = 'Изображение'
    
    def __unicode__(self):
        return self.title