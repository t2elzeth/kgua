from rest_framework import generics

from . import models, serializers


class CharityListAPIView(generics.ListAPIView):
    queryset = models.Charity.objects.all()
    serializer_class = serializers.CharitySerializer


class CharityDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Charity.objects.all()
    serializer_class = serializers.CharitySerializer
