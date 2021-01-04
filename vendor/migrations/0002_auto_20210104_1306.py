# Generated by Django 3.1.4 on 2021-01-04 07:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sellerregistration',
            old_name='FirstName',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='sellerregistration',
            name='LastName',
        ),
        migrations.AddField(
            model_name='sellerregistration',
            name='CompanyName',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
