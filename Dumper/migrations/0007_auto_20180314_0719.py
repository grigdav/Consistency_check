# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-14 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dumper', '0006_auto_20180314_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tf4geenodebm',
            name='field_enodeb_tcunodes',
            field=models.CharField(blank=True, db_column='field_enodeb_tcuNodes', default='', max_length=45, null=True),
        ),
    ]
