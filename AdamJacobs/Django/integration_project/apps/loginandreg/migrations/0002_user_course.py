# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_remove_courses_user'),
        ('loginandreg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='usercourse', to='courses.Courses'),
            preserve_default=False,
        ),
    ]
