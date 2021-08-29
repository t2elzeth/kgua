from rest_framework import generics

from .models import Department
from .serializers import DepartmentSerializer


class DepartmentListAPIView(generics.ListAPIView):
    queryset = Department.objects.all().order_by("-id")
    serializer_class = DepartmentSerializer


class DepartmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
