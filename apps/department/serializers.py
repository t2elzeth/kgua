from . import models
from utils.serializers import MultilanguageModelSerializer
from staff.serializers import StaffSerializer
from rest_framework import serializers


class DepartmentContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DepartmentContacts
        fields = (
            'phone',
            'first_email',
            'second_email'
        )


class DepartmentSerializer(MultilanguageModelSerializer):
    head_teacher = StaffSerializer(source="head_teacher.teacher")
    contacts = DepartmentContactsSerializer()

    class Meta:
        model = models.Department
        fields = ['id', "date_created", 'head_teacher', 'contacts']
