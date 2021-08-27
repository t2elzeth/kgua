from django.db import models
from django.utils.translation import gettext as _

from utils.models import MultilanguageModel, AbstractModelWithGenericSerializer


class News(MultilanguageModel):
    repr_key = "title"
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Новость")
        verbose_name_plural = _("Новости")


class NewsAbstract(AbstractModelWithGenericSerializer):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

    fields = ["title", "description", "image"]

    class Meta:
        abstract = True


class NewsRU(NewsAbstract):
    parent = models.OneToOneField(
        News, on_delete=models.CASCADE, related_name="ru"
    )


class NewsEN(NewsAbstract):
    parent = models.OneToOneField(
        News, on_delete=models.CASCADE, related_name="en"
    )


class NewsKG(NewsAbstract):
    parent = models.OneToOneField(
        News, on_delete=models.CASCADE, related_name="kg"
    )
