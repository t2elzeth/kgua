from modeltranslation.translator import register, TranslationOptions

from . import models


@register(models.Promotion)
class PromotionOptions(TranslationOptions):
    fields = ['title', 'description']
