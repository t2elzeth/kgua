from modeltranslation.translator import TranslationOptions, register

from .models import StaffTraining, StaffScientificWorks, StaffEducation, Staff


@register(StaffTraining)
class StaffTrainingOptions(TranslationOptions):
    fields = ('description',)


@register(StaffScientificWorks)
class StaffScientificWorksOptions(TranslationOptions):
    fields = ['title', 'magazin_name']


@register(StaffEducation)
class StaffEducationOptions(TranslationOptions):
    fields = ['description']


@register(Staff)
class StaffOptions(TranslationOptions):
    fields = ['full_name', 'role']
