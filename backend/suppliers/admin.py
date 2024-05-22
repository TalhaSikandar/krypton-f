from django.contrib import admin
from .models import Supplier
# Register your models here.

# from permissions.models import perm_stores
# perm_stores()

class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'contact', 'address', 'id',
        )


admin.site.register(Supplier, SupplierAdmin)

# Register your models here.
