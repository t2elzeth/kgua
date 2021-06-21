from django.db import models
from django.utils.translation import gettext as _


class ApplicationDocument(models.Model):
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Документ для поступления")
        verbose_name_plural = _("Документы для поступления")
