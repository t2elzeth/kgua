from django.contrib import admin

from .models import Department, DepartmentEN, DepartmentKG, DepartmentRU


class DepartmentENInline(admin.StackedInline):
    model = DepartmentEN


class DepartmentRUInline(admin.StackedInline):
    model = DepartmentRU


class DepartmentKGInline(admin.StackedInline):
    model = DepartmentKG


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    inlines = [DepartmentRUInline, DepartmentKGInline, DepartmentENInline]
