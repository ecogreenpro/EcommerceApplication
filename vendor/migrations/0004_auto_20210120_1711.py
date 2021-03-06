# Generated by Django 3.1.4 on 2021-01-20 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0003_auto_20210104_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerregistration',
            name='NIDImage',
            field=models.FileField(upload_to='Photos/', verbose_name='NID Image'),
        ),
        migrations.AlterField(
            model_name='sellerregistration',
            name='TradeImage',
            field=models.FileField(upload_to='Photos/', verbose_name='Trade License Image'),
        ),
        migrations.CreateModel(
            name='sellerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(max_length=50, unique=True, verbose_name='Company Name')),
                ('Address', models.TextField()),
                ('Phone', models.CharField(max_length=20)),
                ('NID', models.CharField(max_length=50, unique=True)),
                ('TradeLicense', models.CharField(max_length=50, unique=True, verbose_name='Trade License')),
                ('NIDImage', models.ImageField(upload_to='Photos', verbose_name='NID Image')),
                ('TradeImage', models.ImageField(upload_to='Photos', verbose_name='Trade License Image')),
                ('isSeller', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
