# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 23:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170703_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpage',
            old_name='body',
            new_name='content',
        ),
    ]
