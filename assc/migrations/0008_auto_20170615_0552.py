# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assc', '0007_situation_evaluation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='situation',
            name='cie1',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='situation',
            name='cie2',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='situation',
            name='cie3',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='situation',
            name='cie4',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='situation',
            name='cie5',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='situation',
            name='cie6',
            field=models.FloatField(default=0),
        ),
    ]