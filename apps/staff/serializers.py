from rest_framework import serializers

from .models import AdditionalData, Staff, Vacancy


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
    class Meta:
        model = Vacancy
        fields = ["id", "title", "salary", "body", "date_created"]
