from rest_framework import generics

from .models import Vacancy
from .serializers import VacancySerializer


class VacancyListAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all().order_by("-id")
    serializer_class = VacancySerializer


class VacancyDetailAPIView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
