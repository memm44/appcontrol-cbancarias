# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 05:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agregado',
            name='fecha_ag',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='banco',
            name='fecha_b',
            field=models.DateField(),
        ),
    ]
