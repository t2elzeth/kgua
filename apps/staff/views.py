from rest_framework import generics

from .models import Staff, Vacancy
from .serializers import (StaffDetailSerializer, StaffListSerializer,
                          VacancySerializer)


class StaffListAPIView(generics.ListAPIView):
    queryset = Staff.objects.all().order_by("-id")
    serializer_class = StaffListSerializer

    def get_queryset(self):
        return self.queryset[:5]


class StaffDetailAPIView(generics.RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffDetailSerializer


class VacancyListAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all().order_by("-id")
    serializer_class = VacancySerializer
