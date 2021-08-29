from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from .forms import StaffContactsForm
from .models import (
    Staff,
    StaffContacts,
    StaffExperience,
    StaffEducation,
    StaffTraining,
    StaffScientificWorks,
)


class StaffContactsInline(admin.StackedInline):
    model = StaffContacts
    form = StaffContactsForm
    fieldsets = (
        (None, {"fields": ["phone"]}),
        ("Email", {"fields": ["personal_email", "corporate_email"]}),
    )
    can_delete = False


class StaffExperienceInline(admin.StackedInline):
    model = StaffExperience
    can_delete = False


class StaffEducationInline(TranslationStackedInline):
    model = StaffEducation
    extra = 0
    classes = ["collapse"]


class StaffTrainingInline(TranslationStackedInline):
    model = StaffTraining
    extra = 0
    classes = ["collapse"]


class StaffScientificWorksInline(TranslationStackedInline):
    model = StaffScientificWorks
    extra = 0
    classes = ["collapse"]


class MultilanguageModelAdmin(TranslationAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def get_fieldsets(self, request, obj=None):
    #     fieldset_dict = {
    #         'classes': ('collapse',),
    #         'fields': []
    #     }
    #     translated_fields = [
    #         el
    #         for el in obj.__dict__.keys()
    #         if not el.startswith("__")
    #            and not el.endswith("__")
    #     ]
    #     print(translated_fields)
    #     return super().get_fieldsets(request, obj)


@admin.register(Staff)
class StaffAdmin(MultilanguageModelAdmin):
    inlines = [
        StaffContactsInline,
        StaffExperienceInline,
        StaffEducationInline,
        StaffTrainingInline,
        StaffScientificWorksInline,
    ]

    fieldsets = (
        (None, {
            'fields': ('department', 'role', )
        }),
        ('Full Name', {
            'fields': ('full_name_ru', 'full_name_en', 'full_name_ky')
        }),
    )
