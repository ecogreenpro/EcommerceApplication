# Generated by Django 3.1.4 on 2021-01-02 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20201231_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='OrderAmount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]