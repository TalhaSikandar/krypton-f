from django.contrib import admin
from .models import Rawmaterial
# Register your models here.

# from permissions.models import perm_stores
# perm_stores()

class RawmaterialAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'rawmaterial_name',
        )


admin.site.register(Rawmaterial, RawmaterialAdmin)

