# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 12:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backends', '0003_author_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='Age',
            new_name='age',
        ),
    ]
