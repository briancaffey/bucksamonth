# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170422_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='emoji',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
