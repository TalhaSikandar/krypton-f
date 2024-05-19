from django.contrib import admin
from .models import Warehouse
from permissions.models import perm_warehouses
# Register your models here.

perm_warehouses()

class WarehouseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'warehouse_name', 'company',
        )
    prepopulated_fields = {"slug": ("warehouse_name", "company")}


admin.site.register(Warehouse, WarehouseAdmin)
