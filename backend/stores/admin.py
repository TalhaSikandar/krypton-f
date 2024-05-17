from django.contrib import admin
from .models import Store
from permissions.models import perm_stores
# Register your models here.

admin.site.register(Store)
perm_stores()
