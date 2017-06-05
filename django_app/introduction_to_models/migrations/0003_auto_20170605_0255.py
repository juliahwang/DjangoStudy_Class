# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0002_auto_20170605_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='name',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(default='name', max_length=40),
            preserve_default=False,
        ),
    ]