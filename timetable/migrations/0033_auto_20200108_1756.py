# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2020-01-08 17:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0032_pilotoffering'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pilotoffering',
            name='sections',
        ),
        migrations.DeleteModel(
            name='PilotOffering',
        ),
    ]