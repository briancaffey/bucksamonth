# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 06:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_emoji'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
