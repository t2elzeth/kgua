from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from . import models


@admin.register(models.Club)
class ClubAdmin(TranslationAdmin):
    pass
