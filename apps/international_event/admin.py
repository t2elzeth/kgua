from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from django.contrib import admin
from . import models
from utils.admin import MultilanguageModelAdmin


class InternationalEventImageInline(admin.StackedInline):
    model = models.InternationalEventImage
    extra = 0


@admin.register(models.InternationalEvent)
class InternationalEventAdmin(MultilanguageModelAdmin):
    inlines = (
        InternationalEventImageInline,
    )
