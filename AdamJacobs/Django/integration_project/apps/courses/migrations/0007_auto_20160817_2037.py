# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_courses_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courseuser', to='loginandreg.User'),
        ),
    ]
