# Generated by Django 3.1.4 on 2021-01-03 05:54

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20210103_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='longDescirption',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]