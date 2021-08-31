from django.contrib import admin
from django.conf import settings
from modeltranslation.admin import TranslationAdmin
from . import models
from utils.admin import MultilanguageModelAdmin


class CharityImageInline(admin.StackedInline):
    model = models.CharityImage
    extra = 0


@admin.register(models.Charity)
class CharityAdmin(MultilanguageModelAdmin):
    inlines = [CharityImageInline]
