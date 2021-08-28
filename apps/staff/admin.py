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
    StaffEducationEN,
    StaffEducationKG,
    StaffEducationRU,
    StaffTraining,
    StaffTrainingEN,
    StaffTrainingKG,
    StaffTrainingRU,
    StaffScientificWorks,
    StaffScientificWorksEN,
    StaffScientificWorksRU,
    StaffScientificWorksKG
)
from .forms import StaffContactsForm, StaffEducationInlineForm


class StaffENInline(admin.TabularInline):
    model = StaffEN
    can_delete = False
    classes = ["collapse"]


class StaffRUInline(admin.TabularInline):
    model = StaffRU
    can_delete = False
    classes = ["collapse"]


class StaffKGInline(admin.TabularInline):
    model = StaffKG
    can_delete = False
    classes = ["collapse"]


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


class StaffEducationInline(admin.TabularInline):
    model = StaffEducation
    extra = 0
    show_change_link = True
    classes = ['collapse']


class StaffTrainingInline(admin.TabularInline):
    model = StaffTraining
    extra = 0
    show_change_link = True
    classes = ['collapse']


class StaffScientificWorksInline(admin.TabularInline):
    model = StaffScientificWorks
    extra = 0
    show_change_link = True
    classes = ['collapse']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    inlines = [
        StaffRUInline,
        StaffKGInline,
        StaffENInline,
        StaffContactsInline,
        StaffExperienceInline,
        StaffEducationInline,
        StaffTrainingInline,
        StaffScientificWorksInline
    ]

    # class Media:
    #     css = {"all": ("admin_inline.css",)}


class StaffEducationENInline(admin.StackedInline):
    model = StaffEducationEN

    def has_delete_permission(self, request, obj=None):
        return False


class StaffEducationRUInline(admin.StackedInline):
    model = StaffEducationRU

    def has_delete_permission(self, request, obj=None):
        return False


class StaffEducationKGInline(admin.StackedInline):
    model = StaffEducationKG

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(StaffEducation)
class StaffEducationAdmin(admin.ModelAdmin):
    inlines = [StaffEducationRUInline, StaffEducationKGInline, StaffEducationENInline]

    def has_module_permission(self, request):
        return False


class StaffTrainingENInline(admin.StackedInline):
    model = StaffTrainingEN
    can_delete = False


class StaffTrainingRUInline(admin.StackedInline):
    model = StaffTrainingRU
    can_delete = False


class StaffTrainingKGInline(admin.StackedInline):
    model = StaffTrainingKG
    can_delete = False


@admin.register(StaffTraining)
class StaffTrainingAdmin(admin.ModelAdmin):
    inlines = [StaffTrainingRUInline, StaffTrainingKGInline, StaffTrainingENInline]

    def has_module_permission(self, request):
        return False


class StaffScientificWorksENInline(admin.StackedInline):
    model = StaffScientificWorksEN
    can_delete = False


class StaffScientificWorksRUInline(admin.StackedInline):
    model = StaffScientificWorksRU
    can_delete = False


class StaffScientificWorksKGInline(admin.StackedInline):
    model = StaffScientificWorksKG
    can_delete = False


@admin.register(StaffScientificWorks)
class StaffScientificWorksAdmin(admin.ModelAdmin):
    inlines = [StaffScientificWorksRUInline, StaffScientificWorksKGInline, StaffScientificWorksENInline]

    def has_module_permission(self, request):
        return False
