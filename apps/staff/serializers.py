from rest_framework import serializers

from .models import AdditionalData, Staff, Vacancy, VacancyRU, VacancyKG, VacancyEN


class StaffListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ["id", "image", "full_name", "short_position"]


class StaffDetailSerializer(serializers.ModelSerializer):
    additional_data = serializers.SerializerMethodField()

    def get_additional_data(self, staff):
        additionals = AdditionalData.objects.filter(additionals__staff=staff)

        additional_data = {
            additional.title: [
                el.content for el in additional.additionals.all()
            ]
            for additional in additionals
        }

        return additional_data

    class Meta:
        model = Staff
        fields = [
            "id",
            "full_name",
            "image",
            "full_position",
            "experience",
            "image",
            "additional_data",
        ]


class VacancySerializer(serializers.ModelSerializer):
    ru = VacancyRU.get_serializer()
    kg = VacancyKG.get_serializer()
    en = VacancyEN.get_serializer()

    class Meta:
        model = Vacancy
        fields = ['ru', 'kg', 'en', 'date_created']
