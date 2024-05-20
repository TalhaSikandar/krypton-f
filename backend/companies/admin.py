from django.contrib import admin
from .models import Company

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'company_name', 'contact', 'address',
        )


admin.site.register(Company, CompanyAdmin)

