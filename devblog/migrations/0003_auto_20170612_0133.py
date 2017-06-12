# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 23:33
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('devblog', '0002_post_contentspecial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='contentSpecial',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(default=''),
        ),
    ]