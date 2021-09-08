from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from utils.admin import MultilanguageModelAdmin
from . import models


class BureauContactsInline(admin.StackedInline):
    model = models.BureauContacts


class BureauMemberInline(TranslationStackedInline):
    model = models.BureauMember
    extra = 0


@admin.register(models.Bureau)
class BureauAdmin(MultilanguageModelAdmin):
    inlines = [
        BureauContactsInline,
        BureauMemberInline,
    ]
