# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flutter', '0002_auto_20160911_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flut',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
