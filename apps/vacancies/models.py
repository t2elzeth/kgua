from django.db import models
from django.utils.translation import gettext as _

from utils.models import AbstractModelWithGenericSerializer, MultilanguageModel


class Vacancy(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=512)
    description = models.TextField()
    salary = models.IntegerField()

    class Meta:
        verbose_name = _("Вакансия")
        verbose_name_plural = _("Вакансии")
