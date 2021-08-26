from django.contrib import admin

from .models import Club, ClubRU, ClubEN, ClubKG


class ClubENInline(admin.StackedInline):
    model = ClubEN


class ClubRUInline(admin.StackedInline):
    model = ClubRU


class ClubKGInline(admin.StackedInline):
    model = ClubKG


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    inlines = [ClubRUInline, ClubKGInline, ClubENInline]
