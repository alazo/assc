# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assc', '0006_auto_20170614_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='situation',
            name='evaluation',
            field=models.BooleanField(default=False),
        ),
    ]