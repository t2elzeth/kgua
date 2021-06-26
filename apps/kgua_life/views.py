from rest_framework.generics import ListAPIView

from .models import Charity, Event, Jubilee, Promotion
from .serializers import (
    CharitySerializer,
    EventSerializer,
    JubileeSerializer,
    PromotionSerializer,
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
