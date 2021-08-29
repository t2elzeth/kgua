from rest_framework import serializers

from utils.serializers import MultilanguageModelSerializer

from . import models


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventImage
        fields = ["image"]


class EventSerializer(MultilanguageModelSerializer):
    images = EventImageSerializer(many=True)

    class Meta:
        model = models.Event
        fields = ["id", "date_from", "date_to", "images"]
