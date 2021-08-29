from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from . import models


class DepartmentHeadTeacherInline(admin.StackedInline):
    model = models.DepartmentHeadTeacher


class DepartmentContactsInline(admin.StackedInline):
    model = models.DepartmentContacts


@admin.register(models.Department)
class DepartmentAdmin(TranslationAdmin):
    inlines = [DepartmentHeadTeacherInline, DepartmentContactsInline]
