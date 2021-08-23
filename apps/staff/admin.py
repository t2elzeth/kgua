from django.contrib import admin

from .models import AdditionalData, Staff, StaffAdditionalData, Vacancy, VacancyEN, VacancyKG, VacancyRU


class StaffAdditionalDataInline(admin.StackedInline):
    model = StaffAdditionalData
    extra = 0


class VacancyENInline(admin.StackedInline):
    model = VacancyEN

class VacancyRUInline(admin.StackedInline):
    model = VacancyRU

class VacancyKGInline(admin.StackedInline):
    model = VacancyKG


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    inlines = [StaffAdditionalDataInline]

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    inlines =  [VacancyRUInline, VacancyKGInline, VacancyENInline]


admin.site.register(AdditionalData)
