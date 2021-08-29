from utils.serializers import MultilanguageModelSerializer
from . import models


class NewsSerializer(MultilanguageModelSerializer):
    class Meta:
        model = models.News
        fields = ["id", "date_created", 'image']
