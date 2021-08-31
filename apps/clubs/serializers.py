from utils.serializers import MultilanguageModelSerializer
from rest_framework import serializers
from . import models


class ClubImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClubImage
        fields = ['image']


class ClubSerializer(MultilanguageModelSerializer):
    images = ClubImageSerializer(many=True)

    class Meta:
        model = models.Club
        fields = ['id', 'phone', 'images']
