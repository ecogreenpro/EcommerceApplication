# Generated by Django 3.1.4 on 2021-01-19 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_auto_20210119_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerprofile',
            name='NID',
            field=models.CharField(max_length=50),
        ),
    ]