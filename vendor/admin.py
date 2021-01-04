from django.contrib import admin
from .models import SellerRegistration


# Register your models here.
class SellerRegistrationAdmin(admin.ModelAdmin):
    list_display = [
        'Name',
        'CompanyName',
        'Phone',
        'NID',
        'TradeLicense'
    ]

    list_filter = ['Name']
    search_fields = ['CompanyName']


admin.site.register(SellerRegistration, SellerRegistrationAdmin)

