# Generated by Django 3.1.4 on 2021-01-03 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_shipping_isactive'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_id',
            new_name='order_Number',
        ),
    ]