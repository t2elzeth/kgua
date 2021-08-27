from rest_framework import generics

from .models import Staff
from .serializers import StaffSerializer


class StaffListAPIView(generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffDetailAPIView(generics.RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
