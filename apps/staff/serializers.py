from rest_framework import serializers

from utils.serializers import MultilanguageModelSerializer
from .models import (
    Staff,
    StaffContacts,
    StaffContactEmail,
    StaffEducation,
    StaffTraining,
    StaffExperience,
    StaffReward,
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


class StaffExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffExperience
        fields = ("overall", "pedagogical")


class StaffRewardSerializer(MultilanguageModelSerializer):
    class Meta:
        model = StaffReward
        fields = ("year",)


class StaffSerializer(MultilanguageModelSerializer):
    contacts = StaffContactsSerializer()
    experience = StaffExperienceSerializer()
    education = StaffEducationSerializer(many=True)
    trainings = StaffTrainingSerializer(many=True)
    rewards = StaffRewardSerializer(many=True)

    class Meta:
        model = Staff
        fields = (
            "id",
            "contacts",
            "position",
            "image",
            "date_created",
            "experience",
            "education",
            "trainings",
            "rewards",
        )
