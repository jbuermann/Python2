# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='endDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End Date'),
        ),
    ]