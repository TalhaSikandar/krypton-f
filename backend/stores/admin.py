from django.contrib import admin
from .models import Store, StoreProduct
# Register your models here.

from permissions.models import perm_stores
perm_stores()

class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'company', 'manager', 'contact', 'address', 'id',
        )
    prepopulated_fields = {"slug": ("company", "manager")}

admin.site.register(Store, StoreAdmin)
class StoreProductAdmin(admin.ModelAdmin):
    list_display = (
        'store', 'product', 'available_quantity',
        )

admin.site.register(StoreProduct, StoreProductAdmin)

# Register your models here.
