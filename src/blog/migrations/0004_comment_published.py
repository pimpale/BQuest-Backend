# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-14 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190504_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='published',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
