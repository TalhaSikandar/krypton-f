from django.contrib import admin
from .models import Warehouse, WarehouseProduct
# Register your models here.

from permissions.models import perm_warehouses
perm_warehouses()

class WarehouseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'warehouse_name', 'company',
        )
    prepopulated_fields = {"slug": ("warehouse_name", "company")}


class WarehouseProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'warehouse', 'product', 'quantity',
        )
admin.site.register(WarehouseProduct, WarehouseProductAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
