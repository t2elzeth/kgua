from django.db import models


class InternationalEvent(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Международное мероприятие'
        verbose_name_plural = 'Международные мероприятия'


class InternationalProgram(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Международная программа'
        verbose_name_plural = 'Международные программы'


class PartnerOrganization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация-партнер'
        verbose_name_plural = 'Организации-партнеры'
