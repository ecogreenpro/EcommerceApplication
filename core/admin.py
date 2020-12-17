from django.contrib import admin
from .models import Categories,Brands



class CategoriesAdmin(admin.ModelAdmin):
    list_display = [
        'Catagories_photo',
        'name',
        'slug',
        'description', 
        'isactive'
    ]
    list_display_links = ['Catagories_photo','name']
    prepopulated_fields = {'slug': ("name",)}

class BrandsAdmin(admin.ModelAdmin):
    list_display = [
        'brands_photo',
        'name',
        'slug',
        'description',
        'isactive'
    ]
    list_display_links = ['brands_photo','name']
    prepopulated_fields = {'slug': ("name",)}    

admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Brands,BrandsAdmin)
