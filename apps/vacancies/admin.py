from django.contrib import admin

from .models import Vacancy, VacancyEN, VacancyKG, VacancyRU


class VacancyENInline(admin.StackedInline):
    model = VacancyEN


class VacancyRUInline(admin.StackedInline):
    model = VacancyRU


class VacancyKGInline(admin.StackedInline):
    model = VacancyKG


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    inlines = [VacancyRUInline, VacancyKGInline, VacancyENInline]
