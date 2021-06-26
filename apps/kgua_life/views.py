from rest_framework.generics import ListAPIView

from .models import Charity, Event, Promotion
from .serializers import (CharitySerializer, EventSerializer,
                          PromotionSerializer)


class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class PromotionListAPIView(ListAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class CharityListAPIView(ListAPIView):
    queryset = Charity.objects.all()
    serializer_class = CharitySerializer
