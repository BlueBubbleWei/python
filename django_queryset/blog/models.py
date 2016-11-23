from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Blog(models.Model):
    name=models.CharField(max_length=30)
    tagline=models.TextField()

    def __uniicode__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    
    def __unicode__(self):
        return self.name
class Entry(models.Model):
    pk=models.IntegerField(primary_key=True)
    blog=models.ForeignKey(Blog)
    headline=models.CharField(max_length=255)
    body_text=models.TextField()
#    pub_date=DateField()
#    mod_date=DateField()
    authors=models.ManyToManyField(Author)
    n_coments=models.IntegerField()
    n_pingbacks=models.IntegerField()
    rating=models.IntegerField()

    def __unicode__(self):
        return self.headline





