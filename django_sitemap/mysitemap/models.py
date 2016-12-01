from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
    name=models.CharField(max_length=30)
    tagline=models.TextField()

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    def __unicode__(self):
        return self.name

class Entry(models.Model):
    blog=models.ForeignKey(Blog)
    headline=models.CharField(max_length=255)
    body_text=models.TextField()
    pub_date=models.DateField()
    mod_date=models.DateField()
    authors=models.ManyToManyField(Author)
    n_comments=models.IntegerField()
    n_pingbacks=models.IntegerField()
    def __unicode__(self):
        return self.headline



