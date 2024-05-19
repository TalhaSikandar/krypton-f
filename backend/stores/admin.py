from django.contrib import admin
from .models import Store
from permissions.models import perm_stores
# Register your models here.

perm_stores()

class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'company', 'manager', 'contact', 'address', 'id',
        )
    prepopulated_fields = {"slug": ("company", "manager")}


admin.site.register(Store, StoreAdmin)

# Register your models here.
