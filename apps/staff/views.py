from rest_framework import generics

from .models import Staff
from .serializers import StaffSerializer
from . import filters


class StaffListAPIView(generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filterset_class = filters.StaffFilter


class StaffDetailAPIView(generics.RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
