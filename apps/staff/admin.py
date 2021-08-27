from django.contrib import admin
from .models import (
    Staff,
    StaffEN,
    StaffKG,
    StaffRU,
    StaffContacts,
    StaffContactEmail,
    StaffExperience,
    StaffEducation,
)
from .forms import StaffContactsForm


class StaffENInline(admin.StackedInline):
    model = StaffEN


class StaffRUInline(admin.StackedInline):
    model = StaffRU


class StaffKGInline(admin.StackedInline):
    model = StaffKG


class StaffContactsInline(admin.StackedInline):
    model = StaffContacts
    form = StaffContactsForm


class StaffContactEmailInline(admin.StackedInline):
    model = StaffContactEmail


class StaffExperienceInline(admin.StackedInline):
    model = StaffExperience


class StaffEducationInline(admin.StackedInline):
    model = StaffEducation
    extra = 0


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    inlines = [
        StaffRUInline,
        StaffKGInline,
        StaffENInline,
        StaffContactsInline,
        StaffExperienceInline,
        StaffEducationInline,
    ]


# @admin.register(StaffContacts)
# class StaffContactsAdmin(admin.ModelAdmin):
#     inlines = [StaffContactEmailInline]
