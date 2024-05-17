# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'company_code', 'role'
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions', 'role'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('company_code', )
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'company_code','password1', 'password2', 'role', 'first_name', 'last_name')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('company_code', )
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
