from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from utils.admin import MultilanguageModelAdmin
from . import models


@admin.register(models.Vacancy)
class VacancyAdmin(MultilanguageModelAdmin):
    pass
