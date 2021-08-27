from django.db import models

from utils.models import MultilanguageModel, AbstractModelWithGenericSerializer
from django.utils.translation import gettext as _


class Department(MultilanguageModel):
    date_created = models.DateTimeField(auto_now_add=True)
    repr_key = "title"

    class Meta:
        verbose_name = _("Кафедра")
        verbose_name_plural = _("Кафедры")


class DepartmentAbstract(AbstractModelWithGenericSerializer):
    title = models.CharField(max_length=255)

    fields = ['title']

    class Meta:
        abstract = True


class DepartmentRU(DepartmentAbstract):
    parent = models.OneToOneField(Department, on_delete=models.CASCADE, related_name='ru')


class DepartmentEN(DepartmentAbstract):
    parent = models.OneToOneField(Department, on_delete=models.CASCADE, related_name='en')


class DepartmentKG(DepartmentAbstract):
    parent = models.OneToOneField(Department, on_delete=models.CASCADE, related_name='kg')
