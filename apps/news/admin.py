from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import models


@admin.register(models.News)
class NewsAdmin(TranslationAdmin):
    pass
