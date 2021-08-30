from rest_framework import generics

from . import models
from .serializers import ClubSerializer


class ClubListAPIView(generics.ListAPIView):
    queryset = models.Club.objects.all()
    serializer_class = ClubSerializer


class ClubDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Club.objects.all()
    serializer_class = ClubSerializer
