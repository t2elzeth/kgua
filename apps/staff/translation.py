from modeltranslation.translator import TranslationOptions, register

from .models import StaffTraining, StaffScientificWorks, StaffEducation, Staff, StaffReward


@register(StaffTraining)
class StaffTrainingOptions(TranslationOptions):
    fields = ("description",)


@register(StaffScientificWorks)
class StaffScientificWorksOptions(TranslationOptions):
    fields = ["title", "magazin_name"]


@register(StaffEducation)
class StaffEducationOptions(TranslationOptions):
    fields = ["description"]


@register(Staff)
class StaffOptions(TranslationOptions):
    fields = ["full_name"]


@register(StaffReward)
class StaffRewardOptions(TranslationOptions):
    fields = ('description', )
