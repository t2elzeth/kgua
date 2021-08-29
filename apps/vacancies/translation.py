from modeltranslation.translator import TranslationOptions, register

from . import models


@register(models.Vacancy)
class VacanctOptions(TranslationOptions):
    fields = ("title", "description")
