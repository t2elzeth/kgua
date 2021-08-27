from rest_framework import serializers

from .models import Staff, StaffRU, StaffKG, StaffEN, StaffContacts, StaffContactEmail


class StaffContactEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffContactEmail
        fields = ['personal', 'corporate']


class StaffContactsSerializer(serializers.ModelSerializer):
    email = StaffContactEmailSerializer()

    class Meta:
        model = StaffContacts
        fields = ['phone', 'email']


class StaffSerializer(serializers.ModelSerializer):
    ru = StaffRU.get_serializer()
    kg = StaffKG.get_serializer()
    en = StaffEN.get_serializer()
    contacts = StaffContactsSerializer()

    class Meta:
        model = Staff
        fields = ['id', 'ru', 'kg', 'en', 'contacts', 'date_created']
