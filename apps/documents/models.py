from django.db import models


class ApplicationDocument(models.Model):
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Документ для поступления'
        verbose_name_plural = 'Документы для поступления'
