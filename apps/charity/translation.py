from modeltranslation.translator import register, TranslationOptions

from . import models


@register(models.Charity)
class CharityOptions(TranslationOptions):
    fields = ['title', 'description']
