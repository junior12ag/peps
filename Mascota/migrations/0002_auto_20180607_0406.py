# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-07 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mascota', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto',
            field=models.FileField(upload_to=''),
        ),
    ]
