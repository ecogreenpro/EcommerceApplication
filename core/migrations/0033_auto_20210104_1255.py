# Generated by Django 3.1.4 on 2021-01-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20210103_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]