# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-04-18 03:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TEST', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='jugador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TEST.sala')),
            ],
        ),
    ]