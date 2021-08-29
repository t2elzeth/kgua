from modeltranslation.translator import TranslationOptions, register

from .models import Department


@register(Department)
class DepartmentOptions(TranslationOptions):
    fields = ("title", 'description', 'pps_number', 'activities', 'pps_info')
