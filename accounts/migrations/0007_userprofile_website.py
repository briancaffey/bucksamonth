# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-07 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20170507_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]