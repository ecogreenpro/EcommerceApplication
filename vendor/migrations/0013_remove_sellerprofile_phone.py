# Generated by Django 3.1.4 on 2021-01-19 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0012_sellerprofile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellerprofile',
            name='Phone',
        ),
    ]
