# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-05 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplychain', '0003_auto_20170302_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
