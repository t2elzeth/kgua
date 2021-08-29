from utils.serializers import MultilanguageModelSerializer
from . import models


class VacancySerializer(MultilanguageModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = ["id", "date_created", "salary"]
