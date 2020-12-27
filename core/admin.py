from django.contrib import admin
from .models import Categories, Brands, Products, CartProducts, Order


class CategoriesAdmin(admin.ModelAdmin):
    list_display = [
        'Catagories_photo',
        'name',
        'slug',
        'description',
        'isactive'
    ]
    list_display_links = ['Catagories_photo', 'name']
    prepopulated_fields = {'slug': ("name",)}
    list_filter = ['name', 'isactive']
    search_fields = ['name', 'isactive']


class BrandsAdmin(admin.ModelAdmin):
    list_display = [
        'brands_photo',
        'name',
        'slug',
        'description',
        'isactive'
    ]
    list_display_links = ['brands_photo', 'name']
    prepopulated_fields = {'slug': ("name",)}
    list_filter = ['name', 'isactive']
    search_fields = ['name']


class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        'products_photo',
        'name',
        'slug',
        'price',
        'discountPrice',
        'label',
        'stockQuantity',
        'shortDescription',
        'isactive'
    ]
    list_display_links = ['products_photo', 'name']
    prepopulated_fields = {'slug': ("name",)}
    list_filter = ['name', 'isactive', 'category']
    search_fields = ['name']


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(CartProducts)
admin.site.register(Order)
