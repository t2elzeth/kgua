from rest_framework import generics

from . import models, serializers


class JubileeListAPIView(generics.ListAPIView):
    queryset = models.Jubilee.objects.all()
    serializer_class = serializers.JubileeSerializer


class JubileeDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Jubilee.objects.all()
    serializer_class = serializers.JubileeSerializer
