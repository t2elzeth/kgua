from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import models


class PromotionImageInline(admin.StackedInline):
    model = models.PromotionImage
    extra = 0


@admin.register(models.Promotion)
class PromotionAdmin(TranslationAdmin):
    inlines = [PromotionImageInline]
