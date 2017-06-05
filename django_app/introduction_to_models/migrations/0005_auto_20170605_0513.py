# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 05:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0004_auto_20170605_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='teacher_attrs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='introduction_to_models.Person', verbose_name='선생님'),
        ),
    ]
