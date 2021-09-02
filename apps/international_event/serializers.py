from rest_framework import serializers

from utils.serializers import MultilanguageModelSerializer

from . import models


class InternationalEventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InternationalEventImage
        fields = ["image"]


class InternationalEventSerializer(MultilanguageModelSerializer):
    images = InternationalEventImageSerializer(many=True)

    class Meta:
        model = models.InternationalEvent
        fields = ["id", "date_from", "date_to", "images"]
