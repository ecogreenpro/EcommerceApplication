from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils.safestring import mark_safe

Label_Choices = (
    ('Sale', 'Sale'),
    ('New', 'New'),
    ('Flash Sale', 'Flash Sale'),
    ('Promotion', 'Promotion')
)


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='Photos')
    isactive = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:categories", kwargs={'slug': self.slug})

    def Catagories_photo(self):
        return mark_safe('<img src="{}" width="70" height ="70" />'.format(self.image.url))

    Catagories_photo.short_description = 'Image'
    Catagories_photo.allow_tags = True


class Brands(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='Photos')
    isactive = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:brands", kwargs={'slug': self.slug})

    def brands_photo(self):
        return mark_safe('<img src="{}" width="70" height ="70" />'.format(self.image.url))

    brands_photo.short_description = 'Image'
    brands_photo.allow_tags = True


class Products(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    discountPrice = models.FloatField(blank=True, null=True, verbose_name="Discount Price")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    label = models.CharField(choices=Label_Choices, max_length=30)
    stockQuantity = models.CharField(max_length=50, verbose_name="Stock Quantity")
    shortDescription = models.TextField(verbose_name="Short Description")
    longDescirption = models.TextField(verbose_name="Long Description")
    mainImage = models.ImageField(upload_to='Photos', verbose_name="Main Image")
    altImageOne = models.ImageField(upload_to='Photos', verbose_name="Gallery Image One")
    altImageTwo = models.ImageField(upload_to='Photos', verbose_name="Gallery Image Two")
    isactive = models.BooleanField(default=False, verbose_name="Is Active")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:product", kwargs={'slug': self.slug})

    def products_photo(self):
        return mark_safe('<img src="{}" width="70" height ="70" />'.format(self.mainImage.url))

# <<<<<<< Updated upstream
#     # def get_percentage(self):
#     #     Percentage = self.price - (self.price * self.discountPrice / 100)
#     #     return (int)(Percentage)
# =======
#     @property
#     def get_percentage(self):
#         Percentage = ((self.price - self.discountPrice)*100)/self.price
#         return (int)(Percentage)
# >>>>>>> Stashed changes

    products_photo.short_description = 'Image'
    products_photo.allow_tags = True
