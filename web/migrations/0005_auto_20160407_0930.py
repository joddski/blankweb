# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-07 07:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_hiringmanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPostingCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('hiring_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Employee')),
            ],
        ),
        migrations.RemoveField(
            model_name='hiringmanager',
            name='contact',
        ),
        migrations.DeleteModel(
            name='HiringManager',
        ),
    ]
