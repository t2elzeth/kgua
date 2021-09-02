from modeltranslation.translator import TranslationOptions, register

from . import models


@register(models.InternationalEvent)
class InternationalEventOptions(TranslationOptions):
    fields = ("title", "description")
