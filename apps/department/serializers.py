from rest_framework import serializers

from .models import Department, DepartmentRU, DepartmentKG, DepartmentEN


class DepartmentSerializer(serializers.ModelSerializer):
    ru = DepartmentRU.get_serializer()
    kg = DepartmentKG.get_serializer()
    en = DepartmentEN.get_serializer()

    class Meta:
        model = Department
        fields = ['ru', 'kg', 'en', 'date_created']
