from rest_framework.generics import ListAPIView

from .models import Charity, Event, Jubilee, Promotion, Mug, Club
from .serializers import (
    CharitySerializer,
    EventSerializer,
    JubileeSerializer,
    PromotionSerializer,
MugSerializer, ClubSerializer
)


class EventListAPIView(ListAPIView):
    """Список мероприятий"""

    queryset = Event.objects.all()
    serializer_class = EventSerializer


class PromotionListAPIView(ListAPIView):
    """Список акций"""

    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class CharityListAPIView(ListAPIView):
    """Список благотворительных акций"""

    queryset = Charity.objects.all()
    serializer_class = CharitySerializer


class JubileeListAPIView(ListAPIView):
    """Список юбилеев"""

    queryset = Jubilee.objects.all()
    serializer_class = JubileeSerializer

class MugListAPIView(ListAPIView):
    """Список кружков"""

    queryset = Mug.objects.all()
    serializer_class = MugSerializer


class ClubListAPIView(ListAPIView):
    """Список клубов"""

    queryset = Club.objects.all()
    serializer_class = ClubSerializer