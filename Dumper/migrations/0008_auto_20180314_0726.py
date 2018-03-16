# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-14 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dumper', '0007_auto_20180314_0719'),
    ]

    operations = [
        migrations.CreateModel(
            name='ENodeBFunction',
            fields=[
                ('field_enodeb_id', models.CharField(max_length=45, primary_key=True, serialize=False, verbose_name='Station ID')),
                ('field_enodeb_stnnodes', models.CharField(blank=True, db_column='field_enodeb_stnNodes', default='', max_length=45, null=True)),
                ('field_enodeb_tcunodes', models.CharField(blank=True, db_column='field_enodeb_tcuNodes', default='', max_length=45, null=True)),
                ('field_enodeb_nnsfmode', models.CharField(blank=True, db_column='field_enodeb_nnsfMode', default='', max_length=45, null=True)),
                ('field_enodeb_timephasemaxdeviation', models.CharField(blank=True, db_column='field_enodeb_timePhaseMaxDeviation', default='', max_length=45, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TF4GeEnodebM',
        ),
    ]