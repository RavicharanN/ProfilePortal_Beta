# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 11:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20170622_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]
