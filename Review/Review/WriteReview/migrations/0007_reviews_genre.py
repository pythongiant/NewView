# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-08 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WriteReview', '0006_auto_20171005_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='genre',
            field=models.CharField(choices=[('Tech', 'Technology'), ('Movies', 'Movies'), ('Education', 'Education'), ('Art', 'Art'), ('Others', 'Other')], default='Others', max_length=20),
        ),
    ]
