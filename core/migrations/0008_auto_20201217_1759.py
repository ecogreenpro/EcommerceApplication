# Generated by Django 2.2.4 on 2020-12-17 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201217_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='catagory',
            new_name='category',
        ),
    ]
