from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from utils.admin import MultilanguageModelAdmin
from . import models


@admin.register(models.News)
class NewsAdmin(MultilanguageModelAdmin):
    pass
