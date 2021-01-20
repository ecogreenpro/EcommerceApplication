# Generated by Django 3.1.4 on 2021-01-19 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0004_auto_20210119_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerprofile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
