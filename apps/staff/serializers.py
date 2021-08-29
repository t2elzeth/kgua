from rest_framework import serializers

from utils.serializers import MultilanguageModelSerializer
from .models import (
    Staff,
    StaffContacts,
    StaffContactEmail,
    StaffEducation,
    StaffTraining,
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


class StaffTrainingSerializer(MultilanguageModelSerializer):
    class Meta:
        model = StaffTraining
        fields = ["from_year", "to_year"]


class StaffEducationSerializer(MultilanguageModelSerializer):
    class Meta:
        model = StaffEducation
        fields = ["from_year", "to_year"]


class StaffSerializer(MultilanguageModelSerializer):
    contacts = StaffContactsSerializer()
    # experience = StaffExperience()
    education = StaffEducationSerializer(many=True)
    trainings = StaffTrainingSerializer(many=True)

    class Meta:
        model = Staff
        fields = (
            "id",
            "contacts",
            "role",
            "date_created",
            "experience",
            "education",
            "trainings",
        )
