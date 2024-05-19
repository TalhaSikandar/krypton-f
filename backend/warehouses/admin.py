from django.contrib import admin
from .models import Warehouse
# Register your models here.

from permissions.models import perm_warehouses
perm_warehouses()

class WarehouseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'warehouse_name', 'company',
        )
    prepopulated_fields = {"slug": ("warehouse_name", "company")}


admin.site.register(Warehouse, WarehouseAdmin)
