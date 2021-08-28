from modeltranslation.translator import translator, TranslationOptions
from .models import StaffTraining, StaffScientificWorks, StaffEducation, Staff


class StaffTrainingOptions(TranslationOptions):
    fields = ('description', )


class StaffScientificWorksOptions(TranslationOptions):
    fields = ['title', 'magazin_name']


class StaffEducationOptions(TranslationOptions):
    fields = ['description']


class StaffOptions(TranslationOptions):
    fields = ['full_name', 'role']


translator.register(StaffTraining, StaffTrainingOptions)
translator.register(StaffScientificWorks, StaffScientificWorksOptions)
translator.register(StaffEducation, StaffEducationOptions)
translator.register(Staff, StaffOptions)
