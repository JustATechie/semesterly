# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-18 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0018_update_semester_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=1)),
                ('time_start', models.CharField(max_length=15)),
                ('time_end', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='personaltimetable',
            name='events',
            field=models.ManyToManyField(to='student.PersonalEvent'),
        ),
    ]