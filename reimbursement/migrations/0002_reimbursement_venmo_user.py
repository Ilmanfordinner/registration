# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-11 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reimbursement', '0001_reimb_refactor'),
    ]

    operations = [
        migrations.AddField(
            model_name='reimbursement',
            name='venmo_user',
            field=models.CharField(max_length=40,null=True, blank=True),
        ),
    ]
