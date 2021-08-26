from django.contrib import admin

from .models import AdditionalData, Staff, StaffAdditionalData


class StaffAdditionalDataInline(admin.StackedInline):
    model = StaffAdditionalData
    extra = 0


admin.site.register(AdditionalData)
