from rest_framework import serializers

from .models import InternationalEvent, InternationalProgram, PartnerOrganization


class InternationalEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalEvent
        fields = ["name"]


class InternationalProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalProgram
        fields = ["name"]


class PartnerOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerOrganization
        fields = ["name"]
