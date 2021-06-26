from rest_framework.generics import ListAPIView

from .models import InternationalEvent, InternationalProgram, PartnerOrganization
from .serializers import InternationalEventSerializer, InternationalProgramSerializer, PartnerOrganizationSerializer


class InternationalEventListAPIView(ListAPIView):
    """Retrieve list of InternationalEvents required for application"""

    queryset = InternationalEvent.objects.all()
    serializer_class = InternationalEventSerializer


class InternationalProgramListAPIView(ListAPIView):
    """Retrieve list of InternationalPrograms required for application"""

    queryset = InternationalProgram.objects.all()
    serializer_class = InternationalProgramSerializer


class PartnerOrganizationListAPIView(ListAPIView):
    """Retrieve list of PartnerOrganizations required for application"""

    queryset = PartnerOrganization.objects.all()
    serializer_class = PartnerOrganizationSerializer
