from django.db import models

from utils.models import MultilanguageModel, AbstractModelWithGenericSerializer


class Club(MultilanguageModel):
    repr_key = "title"

    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы"


class ClubAbstract(AbstractModelWithGenericSerializer):
    title = models.CharField(max_length=255)
    description = models.TextField()
    supervisor = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    fields = ["title", "description", "supervisor", "phone"]

    class Meta:
        abstract = True


class ClubRU(ClubAbstract):
    parent = models.OneToOneField(
        Club, on_delete=models.CASCADE, related_name="ru"
    )


class ClubEN(ClubAbstract):
    parent = models.OneToOneField(
        Club, on_delete=models.CASCADE, related_name="en"
    )


class ClubKG(ClubAbstract):
    parent = models.OneToOneField(
        Club, on_delete=models.CASCADE, related_name="kg"
    )
