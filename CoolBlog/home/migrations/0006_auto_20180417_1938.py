# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-17 11:38
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180416_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='文章内容'),
        ),
    ]
