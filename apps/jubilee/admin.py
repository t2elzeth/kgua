from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import models


class JubileeImageInline(admin.StackedInline):
    model = models.JubileeImage
    extra = 0


@admin.register(models.Jubilee)
class JubileeAdmin(TranslationAdmin):
    inlines = [JubileeImageInline]
