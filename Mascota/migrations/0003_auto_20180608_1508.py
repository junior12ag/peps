# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-08 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mascota', '0002_auto_20180607_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos'),
        ),
    ]
