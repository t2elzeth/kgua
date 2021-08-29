from rest_framework import generics

from . import models, serializers


class EventListAPIView(generics.ListAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class EventDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
