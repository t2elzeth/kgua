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
    fieldsets = ((None, {'fields': ['phone']}),
                 ('Email', {'fields': ['personal_email', 'corporate_email']}))
    classes = ["collapse"]
    can_delete = False

    class Media:
        css = {"all": ("admin_inline.css",)}


class StaffExperienceInline(admin.StackedInline):
    model = StaffExperience
    can_delete = False
    classes = ['collapse']

    class Media:
        css = {"all": ("admin_inline.css",)}


class StaffEducationInline(TranslationStackedInline):
    model = StaffEducation
    extra = 0
    classes = ['collapse']


class StaffTrainingInline(TranslationStackedInline):
    model = StaffTraining
    extra = 0
    classes = ['collapse']


class StaffScientificWorksInline(TranslationStackedInline):
    model = StaffScientificWorks
    extra = 0
    classes = ['collapse']


@admin.register(Staff)
class StaffAdmin(TranslationAdmin):
    inlines = [
        StaffContactsInline,
        StaffExperienceInline,
        StaffEducationInline,
        StaffTrainingInline,
        StaffScientificWorksInline
    ]

    # class Media:
    #     css = {"all": ("admin_inline.css",)}
