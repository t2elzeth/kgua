from modeltranslation.translator import TranslationOptions, register

from . import models


@register(models.News)
class NewsOptions(TranslationOptions):
    fields = ("title", "description")
