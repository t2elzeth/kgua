from rest_framework import serializers
from staff.serializers import StaffSerializer
from django.conf import settings
from utils.serializers import MultilanguageModelSerializer

from . import models


class BureauContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BureauContacts
        fields = ("phone", "first_email", "second_email", "address")


class BureauMemberSerializer(MultilanguageModelSerializer):
    full_name = serializers.SerializerMethodField(source="member.full_name")

    def get_full_name(self, obj):
        languages = list(map(lambda el: el[0], settings.LANGUAGES))
        query_lang = self.context["request"].query_params.get("lang")
        if query_lang not in languages:
            query_lang = "ru"

        return getattr(obj.member, f"full_name_{query_lang}", obj.member.full_name)

    class Meta:
        model = models.BureauMember
        fields = ("id", "full_name")


class BureauSerializer(MultilanguageModelSerializer):
    contacts = BureauContactsSerializer()
    members = BureauMemberSerializer(many=True)

    class Meta:
        model = models.Bureau
        fields = [
            "id",
            "date_created",
            "contacts",
            "members",
        ]
