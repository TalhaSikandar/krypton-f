from django.contrib import admin
from .models import Product, ProductRawmaterial 
# Register your models here.

# from permissions.models import perm_stores
# perm_stores()

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product_name',
        )

class ProductRawmaterialAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product', 'raw_material', 'required_quantity',
        )

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductRawmaterial, ProductRawmaterialAdmin)

