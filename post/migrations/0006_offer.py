# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_account_cell'),
        ('post', '0005_post_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offerType', models.CharField(choices=[('item', 'Item'), ('money', 'Money')], default='item', max_length=5)),
                ('money', models.IntegerField(default=-1)),
                ('item', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trade', to='post.Post')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy', to='post.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
        ),
    ]
