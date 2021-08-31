from django.db import models


class Charity(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    date = models.DateField()


class CharityImage(models.Model):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()