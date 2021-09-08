from modeltranslation.translator import TranslationOptions, register

from . import models


@register(models.Bureau)
class BureauOptions(TranslationOptions):
    fields = ("title", "activities", "goal", "tasks")


@register(models.BureauMember)
class BureauMemberOptions(TranslationOptions):
    fields = ("position",)
