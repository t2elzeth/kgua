from django.db import models
from django.utils.translation import gettext as _


class News(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = _("Новость")
        verbose_name_plural = _("Новости")
