# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_emoji'),
        ('services', '0002_auto_20170323_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('votes', models.IntegerField(default=0)),
                ('emoji', models.CharField(default='', max_length=20)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_commenter', to='accounts.UserProfile')),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='review_user',
        ),
        migrations.RemoveField(
            model_name='review',
            name='reviewed_service',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]