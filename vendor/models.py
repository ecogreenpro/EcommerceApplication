from django.db import models


# Create your models here.
class SellerRegistration(models.Model):
    Name = models.CharField(max_length=50)
    CompanyName = models.CharField(max_length=50, unique=True, verbose_name='Company Name')
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    Address = models.TextField()
    NID = models.CharField(max_length=50)
    TradeLicense = models.CharField(max_length=50, verbose_name='Trade License')
    NIDImage = models.ImageField(upload_to='Photos', verbose_name='NID Image')
    TradeImage = models.ImageField(upload_to='Photos', verbose_name='Trade License Image')

    def __str__(self):
        return self.CompanyName
