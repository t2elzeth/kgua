from modeltranslation.translator import TranslationOptions, register

from . import models


@register(models.Department)
class DepartmentOptions(TranslationOptions):
    fields = ("title", "description", "pps_number", "activities", "pps_info")


@register(models.DepartmentReward)
class DepartmentRewardOptions(TranslationOptions):
    fields = ("description",)
