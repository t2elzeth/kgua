from rest_framework.generics import ListAPIView

from .models import Charity, Event, Promotion
from .serializers import (CharitySerializer, EventSerializer,
                          PromotionSerializer)


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
