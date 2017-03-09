# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-09 12:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplychain', '0006_auto_20170309_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='comment',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='part', to='supplychain.Product'),
        ),
    ]
