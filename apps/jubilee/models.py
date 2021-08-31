from django.db import models


class Jubilee(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    date = models.DateField()


class JubileeImage(models.Model):
    Jubilee = models.ForeignKey(Jubilee, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()
