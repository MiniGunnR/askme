# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-01 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0003_auto_20160301_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='not_an_answer',
            field=models.BooleanField(default=False),
        ),
    ]
