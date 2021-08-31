from modeltranslation.translator import register, TranslationOptions

from . import models


@register(models.Jubilee)
class JubileeOptions(TranslationOptions):
    fields = ['title', 'description']
