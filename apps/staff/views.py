from rest_framework import generics

from .models import Staff
from .serializers import StaffDetailSerializer, StaffListSerializer


class StaffListAPIView(generics.ListAPIView):
    queryset = Staff.objects.all().order_by("-id")
    serializer_class = StaffListSerializer

    def get_queryset(self):
        return self.queryset[:5]


class StaffDetailAPIView(generics.RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffDetailSerializer
