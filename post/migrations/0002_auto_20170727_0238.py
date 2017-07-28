# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='use',
            field=models.CharField(choices=[('office', 'Office Use'), ('academic', 'Academic Use')], default='office', max_length=8),
        ),
    ]
