from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from . import models


class ClubImageInline(admin.StackedInline):
    model = models.ClubImage
    extra = 0


@admin.register(models.Club)
class ClubAdmin(TranslationAdmin):
    inlines = [ClubImageInline]
