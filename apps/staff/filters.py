import django_filters

from . import models


class StaffFilter(django_filters.rest_framework.FilterSet):
    position = django_filters.CharFilter(field_name="position", lookup_expr='iexact')

    class Meta:
        model = models.Staff
        fields = ("position",)
