from rest_framework import serializers

from .models import Vacancy, VacancyRU, VacancyKG, VacancyEN


class VacancySerializer(serializers.ModelSerializer):
    ru = VacancyRU.get_serializer()
    kg = VacancyKG.get_serializer()
    en = VacancyEN.get_serializer()

    class Meta:
        model = Vacancy
        fields = ['ru', 'kg', 'en', 'date_created']