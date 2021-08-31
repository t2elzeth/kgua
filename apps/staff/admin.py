from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from utils.admin import MultilanguageModelAdmin
from .forms import StaffContactsForm
from .models import (
    Staff,
    StaffContacts,
    StaffEducation,
    StaffExperience,
    StaffReward,
    StaffScientificWorks,
    StaffTraining,
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


class StaffRewardInline(TranslationStackedInline):
    model = StaffReward
    extra = 0
    classes = ("collapse",)


@admin.register(Staff)
class StaffAdmin(MultilanguageModelAdmin):
    inlines = [
        StaffContactsInline,
        StaffExperienceInline,
        StaffEducationInline,
        StaffTrainingInline,
        StaffScientificWorksInline,
        StaffRewardInline,
    ]
