# Generated by Django 3.1.4 on 2021-01-20 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0019_auto_20210119_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('CompanyName', models.CharField(max_length=50, unique=True, verbose_name='Company Name')),
                ('Phone', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.TextField()),
                ('NID', models.CharField(max_length=50)),
                ('TradeLicense', models.CharField(max_length=50, verbose_name='Trade License')),
                ('NIDImage', models.FileField(upload_to='Photos/', verbose_name='NID Image')),
                ('TradeImage', models.FileField(upload_to='Photos/', verbose_name='Trade License Image')),
            ],
        ),
    ]
