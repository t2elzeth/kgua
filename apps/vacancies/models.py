from django.db import models

from utils.models import MultilanguageModel, AbstractModelWithGenericSerializer
from django.utils.translation import gettext as _


class Vacancy(MultilanguageModel):
    date_created = models.DateTimeField(auto_now_add=True)
    repr_key = "title"

    class Meta:
        verbose_name = _("Вакансия")
        verbose_name_plural = _("Вакансии")


class VacancyAbstract(AbstractModelWithGenericSerializer):
    title = models.CharField(max_length=255)
    body = models.TextField()
    salary = models.CharField(max_length=255)

    fields = ["title", "body", "salary"]

    class Meta:
        abstract = True


class VacancyRU(VacancyAbstract):
    parent = models.OneToOneField(
        Vacancy, on_delete=models.CASCADE, related_name="ru"
    )


class VacancyEN(VacancyAbstract):
    parent = models.OneToOneField(
        Vacancy, on_delete=models.CASCADE, related_name="en"
    )


class VacancyKG(VacancyAbstract):
    parent = models.OneToOneField(
        Vacancy, on_delete=models.CASCADE, related_name="kg"
    )
