# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_emoji'),
        ('services', '0014_subscription_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ManyToManyField(to='categories.Category'),
        ),
    ]