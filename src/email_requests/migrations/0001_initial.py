# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_remove_profile_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_body', models.TextField(blank=True, default='')),
                ('preferred_email', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('mentee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Profile')),
                ('mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Mentor')),
            ],
        ),
    ]
