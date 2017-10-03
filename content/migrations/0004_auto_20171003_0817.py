# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20171001_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shexpjob',
            name='iceberg',
            field=models.FileField(upload_to='ShExp/Job/Ice'),
        ),
        migrations.AlterField(
            model_name='shexpjob',
            name='imgcov',
            field=models.FileField(upload_to='ShExp/Job/Cov'),
        ),
        migrations.AlterField(
            model_name='shexpman',
            name='imgcov',
            field=models.FileField(upload_to='ShExp/Man/Cov'),
        ),
        migrations.AlterField(
            model_name='shexpman',
            name='imgdis',
            field=models.FileField(upload_to='ShExp/Man/Dis'),
        ),
    ]
