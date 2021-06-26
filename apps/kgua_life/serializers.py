from rest_framework import serializers

from .models import Charity, Event, Promotion, Jubilee


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["title", "description", "date", "date_created", "is_active"]


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ["title"]


class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = ["title"]


class JubileeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jubilee
        fields = ["title"]
