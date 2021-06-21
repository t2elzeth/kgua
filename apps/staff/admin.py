from django.contrib import admin

from .models import (Staff, AdditionalData, StaffAdditionalData)


class StaffAdditionalDataInline(admin.StackedInline):
    model = StaffAdditionalData
    extra = 0


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    inlines = [
        StaffAdditionalDataInline
    ]


admin.site.register(AdditionalData)
