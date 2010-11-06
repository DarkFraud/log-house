# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save, pre_delete
from loghouse.utils import *

class Image(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Название')
    file = models.ImageField(upload_to = 'images/Images/', verbose_name = 'Изображение')
    
    class Meta:
        verbose_name_plural = 'Изображения'
        verbose_name = 'Изображение'
    
    def __unicode__(self):
        return self.title
    
    def get_thumbnail_html(self):
        html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
        return html % (self.file.url, get_thumbnail_url(self.file.url), self.title)
    get_thumbnail_html.short_description = 'Изображение'
    get_thumbnail_html.allow_tags = True

def post_save_handler(sender, **kwargs):
    create_thumbnail(kwargs['instance'].file.path)
post_save.connect(post_save_handler, sender=Image)

def pre_delete_handler(sender, **kwargs):
    delete_thumbnail(kwargs['instance'].file.path)
pre_delete.connect(pre_delete_handler, sender=Image)