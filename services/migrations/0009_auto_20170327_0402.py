# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_interest_serviceinterest_userinterest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='interest',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
