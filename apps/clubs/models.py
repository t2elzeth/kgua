from django.db import models


class Club(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    supervisor = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы"


class ClubImage(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()
