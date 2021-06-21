from rest_framework import generics

from .models import News
from .serializers import NewsSerializer


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all().order_by("-id")
    serializer_class = NewsSerializer

    def get_queryset(self):
        return self.queryset[:5]


class NewsDetailAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
