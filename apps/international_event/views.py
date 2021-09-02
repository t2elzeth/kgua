from rest_framework import generics

from . import models, serializers


class InternationalEventListAPIView(generics.ListAPIView):
    queryset = models.InternationalEvent.objects.all()
    serializer_class = serializers.InternationalEventSerializer


class InternationalEventDetailAPIView(generics.RetrieveAPIView):
    queryset = models.InternationalEvent.objects.all()
    serializer_class = serializers.InternationalEventSerializer
