# Generated by Django 3.1.4 on 2021-01-19 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0009_auto_20210119_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerprofile',
            name='NID',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='sellerprofile',
            name='Phone',
            field=models.CharField(max_length=20),
        ),
    ]
