from rest_framework import serializers

from . import models
from utils.serializers import MultilanguageModelSerializer


class PromotionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PromotionImage
        fields = ['image']


class PromotionSerializer(MultilanguageModelSerializer):
    images = PromotionImageSerializer(many=True)

    class Meta:
        model = models.Promotion
        fields = ('id', 'images', 'date_from', 'date_to')
