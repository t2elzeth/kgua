from modeltranslation.translator import register, TranslationOptions

from . import models


@register(models.Club)
class ClubOptions(TranslationOptions):
    fields = ['title', 'description', 'supervisor']