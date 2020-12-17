from django.contrib import admin
from .models import Categories



class CategoriesAdmin(admin.ModelAdmin):
    list_display = [
        'Catagories_photo',
        'name',
        'slug',
        'description',
        
        'isactive'
    ]
    prepopulated_fields = {'slug': ("name",)}
    

admin.site.register(Categories,CategoriesAdmin)
