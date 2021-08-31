from django.contrib import admin

from modeltranslation.admin import TranslationAdmin
from . import models


class CharityImageInline(admin.StackedInline):
    model = models.CharityImage
    extra = 0


@admin.register(models.Charity)
class CharityAdmin(TranslationAdmin):
    inlines = [CharityImageInline]
