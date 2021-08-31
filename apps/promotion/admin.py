from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from utils.admin import MultilanguageModelAdmin
from . import models


class PromotionImageInline(admin.StackedInline):
    model = models.PromotionImage
    extra = 0


@admin.register(models.Promotion)
class PromotionAdmin(MultilanguageModelAdmin):
    inlines = [PromotionImageInline]
