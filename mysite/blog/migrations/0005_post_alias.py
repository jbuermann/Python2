# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170626_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alias',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
