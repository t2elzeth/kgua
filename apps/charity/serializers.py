from rest_framework import serializers
from utils.serializers import MultilanguageModelSerializer
from . import models


class CharityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CharityImage
        fields = ['image']


class CharitySerializer(MultilanguageModelSerializer):
    images = CharityImageSerializer(many=True)

    class Meta:
        model = models.Charity
        fields = ('id', 'images')
