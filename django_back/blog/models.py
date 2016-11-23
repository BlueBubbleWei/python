# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import  python_2_unicode_compatible
# Create your models here.

class Article(models.Model):
    title=models.CharField('title',max_length=256)
    content=models.TextField('CONTENT')
    pub_date=models.DateTimeField('pub_date',auto_now_add=True,editable=True)
    upd_date=models.DateTimeField('updateTime',auto_now=True,null=True)
    def __unicode__(self):
        return self.title

class Person(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    def my_property(self):
        return self.first_name+'  '+last_name

    my_property.short_description='Full name of the person'
    full_name=property(my_property)
