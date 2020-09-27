# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-11-16 00:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0010_draft_app'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='tshirt_size',
            field=models.CharField(choices=[("Women's - XXS", "Women's - XXS"), ("Women's - XS", "Women's - XS"), ("Women's - S", "Women's - S"), ("Women's - M", "Women's - M"), ("Women's - L", "Women's - L"), ("Women's - XL", "Women's - XL"), ("Women's - XXL", "Women's - XXL"), ('Unisex - XXS', 'Unisex - XXS'), ('Unisex - XS', 'Unisex - XS'), ('Unisex - S', 'Unisex - S'), ('Unisex - M', 'Unisex - M'), ('Unisex - L', 'Unisex - L'), ('Unisex - XL', 'Unisex - XL'), ('Unisex - XXL', 'Unisex - XXL')], default='Unisex - M', max_length=3),
        ),
    ]
