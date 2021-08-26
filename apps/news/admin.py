from django.contrib import admin

from .models import News, NewsRU, NewsEN, NewsKG


class NewsENInline(admin.StackedInline):
    model = NewsEN


class NewsRUInline(admin.StackedInline):
    model = NewsRU


class NewsKGInline(admin.StackedInline):
    model = NewsKG


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsRUInline, NewsKGInline, NewsENInline]
