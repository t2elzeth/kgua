from rest_framework import generics

from .models import Bureau
from .serializers import BureauSerializer


class BureauListAPIView(generics.ListAPIView):
    queryset = Bureau.objects.all().order_by("-id")
    serializer_class = BureauSerializer


class BureauDetailAPIView(generics.RetrieveAPIView):
    queryset = Bureau.objects.all()
    serializer_class = BureauSerializer
