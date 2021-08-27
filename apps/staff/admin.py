from django.contrib import admin

from .models import Staff, StaffEN, StaffKG, StaffRU


class StaffENInline(admin.StackedInline):
    model = StaffEN


class StaffRUInline(admin.StackedInline):
    model = StaffRU


class StaffKGInline(admin.StackedInline):
    model = StaffKG


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    inlines = [StaffRUInline, StaffKGInline, StaffENInline]
