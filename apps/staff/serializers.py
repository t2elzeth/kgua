from rest_framework import serializers

from .models import (
    Staff,
    StaffRU,
    StaffKG,
    StaffEN,
    StaffContacts,
    StaffContactEmail,
    StaffExperience,
    StaffEducation,
StaffEducationRU,
StaffEducationEN,
StaffEducationKG
)


class StaffContactEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffContactEmail
        fields = ["personal", "corporate"]


class StaffContactsSerializer(serializers.ModelSerializer):
    email = StaffContactEmailSerializer()

    class Meta:
        model = StaffContacts
        fields = ["phone", "email"]


class StaffExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffExperience
        fields = ["overall", "pedagogical"]


class StaffEducationSerializer(serializers.ModelSerializer):
    ru = StaffEducationRU.get_serializer()
    kg = StaffEducationKG.get_serializer()
    en = StaffEducationEN.get_serializer()

    class Meta:
        model = StaffEducation
        fields = ["from_year", "to_year", "ru", "en", "kg"]


class StaffSerializer(serializers.ModelSerializer):
    ru = StaffRU.get_serializer()
    kg = StaffKG.get_serializer()
    en = StaffEN.get_serializer()
    contacts = StaffContactsSerializer()
    experience = StaffExperience()
    education = StaffEducationSerializer(many=True)

    class Meta:
        model = Staff
        fields = (
            "id",
            "ru",
            "kg",
            "en",
            "contacts",
            "date_created",
            "experience",
            "education",
        )
