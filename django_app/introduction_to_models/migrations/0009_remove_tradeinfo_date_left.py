# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 09:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0008_auto_20170605_0728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tradeinfo',
            name='date_left',
        ),
    ]