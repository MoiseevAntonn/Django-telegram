# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-30 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link_with_email',
            name='chat_id',
            field=models.IntegerField(max_length=40),
        ),
    ]