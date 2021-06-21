from django.db import models


class ApplicationDocument(models.Model):
    content = models.CharField(max_length=255)
