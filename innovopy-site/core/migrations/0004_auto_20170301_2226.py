# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-01 22:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170215_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='InnovoUserPublication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='innovouser',
            name='degree_type',
            field=models.IntegerField(blank=True, choices=[(0, 'N/A'), (1, 'Associates'), (2, 'B.A.'), (3, 'B.S.'), (4, 'M.A.'), (5, 'M.S.'), (6, 'Ph.D.'), (7, 'D.Sc.'), (8, 'In Progress')], default=0),
        ),
        migrations.AddField(
            model_name='innovouserpublication',
            name='innovouser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.InnovoUser'),
        ),
        migrations.AddField(
            model_name='innovouserpublication',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Publication'),
        ),
    ]