from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from django.contrib import admin
from . import models


class EventImageInline(admin.StackedInline):
    model = models.EventImage
    extra = 0


@admin.register(models.Event)
class EventAdmin(TranslationAdmin):
    inlines = (
        EventImageInline,
    )
