# Generated by Django 3.1.4 on 2021-01-02 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20210102_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]