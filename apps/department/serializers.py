from rest_framework import serializers
from staff.serializers import StaffSerializer

from utils.serializers import MultilanguageModelSerializer

from . import models


class DepartmentContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DepartmentContacts
        fields = ("phone", "first_email", "second_email")


class DepartmentRewardSerializer(MultilanguageModelSerializer):
    class Meta:
        model = models.DepartmentReward
        fields = ("date",)


class DepartmentSerializer(MultilanguageModelSerializer):
    head_teacher = StaffSerializer(source="head_teacher.teacher")
    contacts = DepartmentContactsSerializer()
    rewards = DepartmentRewardSerializer(many=True)
    teachers = StaffSerializer(many=True)

    class Meta:
        model = models.Department
        fields = [
            "id",
            "date_created",
            "head_teacher",
            "contacts",
            "rewards",
            "teachers",
        ]
