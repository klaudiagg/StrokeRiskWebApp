# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-08 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0007_auto_20180808_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='Question',
        ),
        migrations.DeleteModel(
            name='Results',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
