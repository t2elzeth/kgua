import django_filters
from django.conf import settings
from . import models


class StaffFilter(django_filters.rest_framework.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        languages = list(map(lambda el: el[0], settings.LANGUAGES))
        query_lang = self.request.query_params.get('lang')

        if query_lang not in languages:
            query_lang = 'ru'

        self.filters['full_name'].field_name += f"_{query_lang}"

    position = django_filters.CharFilter(field_name="position", lookup_expr='iexact')
    full_name = django_filters.CharFilter(field_name="full_name", lookup_expr='icontains')
