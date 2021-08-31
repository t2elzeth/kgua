from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from utils.admin import MultilanguageModelAdmin
from . import models


class JubileeImageInline(admin.StackedInline):
    model = models.JubileeImage
    extra = 0


@admin.register(models.Jubilee)
class JubileeAdmin(MultilanguageModelAdmin):
    inlines = [JubileeImageInline]
