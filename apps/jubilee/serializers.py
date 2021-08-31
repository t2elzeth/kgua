from rest_framework import serializers

from . import models
from utils.serializers import MultilanguageModelSerializer


class JubileeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JubileeImage
        fields = ['image']


class JubileeSerializer(MultilanguageModelSerializer):
    images = JubileeImageSerializer(many=True)

    class Meta:
        model = models.Jubilee
        fields = ('id', 'images', 'date')
