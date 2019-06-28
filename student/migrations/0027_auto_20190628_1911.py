# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2019-06-28 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0033_pilotsection'),
        ('student', '0026_student_sis_enabled'),
    ]

    operations = [
        migrations.CreateModel(
            name='PILOTOffering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_size', models.IntegerField(default=-1)),
                ('start_time', models.CharField(max_length=15)),
                ('end_time', models.CharField(max_length=15)),
                ('day', models.CharField(max_length=1)),
                ('location', models.CharField(default=b'TBA', max_length=200)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.PILOTSection')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='pre_health',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='pre_law',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pilotoffering',
            name='students',
            field=models.ManyToManyField(blank=True, to='student.Student'),
        ),
    ]
