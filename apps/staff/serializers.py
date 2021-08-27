from rest_framework import serializers

from .models import Staff, StaffRU, StaffKG, StaffEN


class StaffSerializer(serializers.ModelSerializer):
    ru = StaffRU.get_serializer()
    kg = StaffKG.get_serializer()
    en = StaffEN.get_serializer()

    class Meta:
        model = Staff
        fields = ['ru', 'kg', 'en', 'date_created']
