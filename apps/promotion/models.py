from django.db import models


class Promotion(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    date_from = models.DateField()
    date_to = models.DateField()

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


class PromotionImage(models.Model):
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()
