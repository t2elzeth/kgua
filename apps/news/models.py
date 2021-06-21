from django.db import models
from django.utils.translation import gettext as _


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:20]

    class Meta:
        verbose_name = _("Новость")
        verbose_name_plural = _("Новости")
