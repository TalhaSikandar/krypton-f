from django.contrib import admin
from .models import Supplier, SupplierRawmaterial
# Register your models here.

# from permissions.models import perm_stores
# perm_stores()

class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'contact', 'address', 'id',
        )


admin.site.register(Supplier, SupplierAdmin)

# Register your models here.
class SupplierRawmaterialAdmin(admin.ModelAdmin):
    list_display = (
        'supplier', 'rawmaterial', 'available_quantity',
        )

admin.site.register(SupplierRawmaterial, SupplierRawmaterialAdmin)

