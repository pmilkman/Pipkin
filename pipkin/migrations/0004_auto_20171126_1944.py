# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipkin', '0003_auto_20171126_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='person',
            name='token',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
