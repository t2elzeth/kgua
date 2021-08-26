from rest_framework import serializers

from .models import Club, ClubEN, ClubKG, ClubRU


class ClubSerializer(serializers.ModelSerializer):
    ru = ClubRU.get_serializer()
    kg = ClubKG.get_serializer()
    en = ClubEN.get_serializer()

    class Meta:
        model = Club
        fields = ['ru', 'kg', 'en']

    # def get_field_names(self, declared_fields, info):
    #     res = super().get_field_names(declared_fields, info)
    #     print('This is modelfields', res)
    #     return res
