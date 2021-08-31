from rest_framework import generics

from . import models, serializers


class PromotionListAPIView(generics.ListAPIView):
    queryset = models.Promotion.objects.all()
    serializer_class = serializers.PromotionSerializer


class PromotionDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Promotion.objects.all()
    serializer_class = serializers.PromotionSerializer
