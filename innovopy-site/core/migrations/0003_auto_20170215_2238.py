# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-15 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170215_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innovouser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='innovouser',
            name='prev_positions',
            field=models.TextField(blank=True, null=True),
        ),
    ]