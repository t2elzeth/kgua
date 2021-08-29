from modeltranslation.translator import TranslationOptions, register

from . import models


@register(models.Event)
class EventOptions(TranslationOptions):
    fields = ("title", "description")
