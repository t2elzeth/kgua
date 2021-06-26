from django.db import models


class InternationalEvent(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class InternationalProgram(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PartnerOrganization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
