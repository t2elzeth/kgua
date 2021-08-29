from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from . import models


class DepartmentHeadTeacherInline(admin.StackedInline):
    model = models.DepartmentHeadTeacher


class DepartmentContactsInline(admin.StackedInline):
    model = models.DepartmentContacts


class DepartmentRewardInline(TranslationStackedInline):
    model = models.DepartmentReward
    extra = 0
    classes = ('collapse',)


@admin.register(models.Department)
class DepartmentAdmin(TranslationAdmin):
    inlines = [DepartmentHeadTeacherInline, DepartmentContactsInline, DepartmentRewardInline]
