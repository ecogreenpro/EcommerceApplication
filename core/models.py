from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils.safestring import mark_safe


class Categories(models.Model):
    name = models.CharField(max_length= 100)
    slug= models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to = 'Photos')
    isactive= models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:categories", kwargs={'slug': self.slug})    
    
    def Catagories_photo(self):
        return mark_safe('<img src="{}" width="70" height ="70" />'.format(self.image.url))
    Catagories_photo.short_description = 'Image'
    Catagories_photo.allow_tags = True

class Brands(models.Model):
    name = models.CharField(max_length= 100)
    slug= models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to = 'Photos')
    isactive= models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:brands", kwargs={'slug': self.slug})    
    
    def brands_photo(self):
        return mark_safe('<img src="{}" width="70" height ="70" />'.format(self.image.url))
    brands_photo.short_description = 'Image'
    brands_photo.allow_tags = True