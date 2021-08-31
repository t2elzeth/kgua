from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from . import models
from utils.admin import MultilanguageModelAdmin


class ClubImageInline(admin.StackedInline):
    model = models.ClubImage
    extra = 0


@admin.register(models.Club)
class ClubAdmin(MultilanguageModelAdmin):
    inlines = [ClubImageInline]
