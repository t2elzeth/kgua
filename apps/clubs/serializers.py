from utils.serializers import MultilanguageModelSerializer

from . import models


class ClubSerializer(MultilanguageModelSerializer):
    class Meta:
        model = models.Club
        fields = ['id', 'phone']
