from rest_framework import serializers

from .models import Staff, StaffRU, StaffKG, StaffEN, StaffContacts, StaffContactEmail, StaffExperience


class StaffContactEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffContactEmail
        fields = ['personal', 'corporate']


class StaffContactsSerializer(serializers.ModelSerializer):
    email = StaffContactEmailSerializer()

    class Meta:
        model = StaffContacts
        fields = ['phone', 'email']


class StaffExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffExperience
        fields = ['overall', 'pedagogical']


class StaffSerializer(serializers.ModelSerializer):
    ru = StaffRU.get_serializer()
    kg = StaffKG.get_serializer()
    en = StaffEN.get_serializer()
    contacts = StaffContactsSerializer()
    experience = StaffExperience()

    class Meta:
        model = Staff
        fields = ('id', 'ru', 'kg', 'en', 'contacts', 'date_created', 'experience')
