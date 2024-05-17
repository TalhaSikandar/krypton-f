from django.contrib import admin

from .models import Address, Contact
# Register your models here.

admin.site.register(Contact)
admin.site.register(Address)
