# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-28 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0008_update_apps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='reimb',
            field=models.BooleanField(default=False),
        ),
    ]
