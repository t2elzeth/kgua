from rest_framework import serializers

from .models import News, NewsEN, NewsKG, NewsRU


class NewsSerializer(serializers.ModelSerializer):
    ru = NewsRU.get_serializer()
    kg = NewsKG.get_serializer()
    en = NewsEN.get_serializer()

    class Meta:
        model = News
        fields = ['ru', 'kg', 'en', 'date_created']
