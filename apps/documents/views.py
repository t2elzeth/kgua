from rest_framework.generics import ListAPIView

from .models import ApplicationDocument
from .serializers import ApplicationDocumentSerializer


class ApplicationDocumentListAPIView(ListAPIView):
    """Retrieve list of ApplicationDocuments required for application"""

    queryset = ApplicationDocument.objects.all()
    serializer_class = ApplicationDocumentSerializer
