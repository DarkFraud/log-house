# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save, pre_delete
from loghouse.utils import *
from loghouse.project.models import Project

class Picture(models.Model):
    picture = models.ImageField(upload_to='images/Phote/Picture', max_length=250, verbose_name = 'Фотография')
    description = models.CharField(max_length=250, blank=True, verbose_name = 'Описание')
    
    class Meta:
        verbose_name_plural = 'Фотографии'
        verbose_name = 'Фотография'
        
    def __unicode__(self):
        return self.description
        
    def get_thumbnail_html(self):
        html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
        return html % (self.picture.url, get_thumbnail_url(self.picture.url), self.description)
    get_thumbnail_html.short_description = 'Фотография'
    get_thumbnail_html.allow_tags = True

def post_save_picture(sender, **kwargs):
    create_thumbnail(kwargs['instance'].picture.path)
post_save.connect(post_save_picture, sender=Picture)

def pre_delete_picture(sender, **kwargs):
    delete_thumbnail(kwargs['instance'].picture.path)
pre_delete.connect(pre_delete_picture, sender=Picture)

class Album(models.Model):
    album_cover = models.ImageField(upload_to='images/Phote/Picture', max_length=250, verbose_name = 'Обложка')
    project = models.ForeignKey(Project, verbose_name = 'Проект')
    content = models.TextField(verbose_name = 'Контент')
    
    class Meta:
        verbose_name_plural = 'Альбомы проектов'
        verbose_name = 'Альбом проекта'
    
    def __unicode__(self):
        return self.project.title
    
    def get_thumbnail_html(self):
        html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
        return html % (self.album_cover.url, get_thumbnail_url(self.album_cover.url), self.project)
    get_thumbnail_html.short_description = 'Обложка'
    get_thumbnail_html.allow_tags = True

def post_save_album(sender, **kwargs):
    create_thumbnail(kwargs['instance'].album_cover.path)
post_save.connect(post_save_album, sender=Album)

def pre_delete_album(sender, **kwargs):
    delete_thumbnail(kwargs['instance'].album_cover.path)
pre_delete.connect(pre_delete_album, sender=Album)

class OtherAlbum(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Название')
    other_album_cover = models.ImageField(upload_to='images/Phote/Picture', max_length=250, verbose_name = 'Обложка')
    pictures = models.ManyToManyField(Picture, verbose_name = 'Фотографии')
    
    class Meta:
        verbose_name_plural = 'Альбомы'
        verbose_name = 'Альбом'
    
    def __unicode__(self):
        return self.title
    
    def get_thumbnail_html(self):
        html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
        return html % (self.other_album_cover.url, get_thumbnail_url(self.other_album_cover.url), self.title)
    get_thumbnail_html.short_description = 'Обложка'
    get_thumbnail_html.allow_tags = True
    
def post_save_other(sender, **kwargs):
    create_thumbnail(kwargs['instance'].other_album_cover.path)
post_save.connect(post_save_other, sender=OtherAlbum)

def pre_delete_other(sender, **kwargs):
    delete_thumbnail(kwargs['instance'].other_album_cover.path)
pre_delete.connect(pre_delete_other, sender=OtherAlbum)