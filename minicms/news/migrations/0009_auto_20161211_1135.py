# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-11 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20161211_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(max_length=255, unique=True, verbose_name='\u7f51\u5740'),
        ),
    ]
