from django.db import models
from django.utils.translation import gettext as _
from rest_framework import serializers

class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    short_position = models.CharField(max_length=255)
    full_position = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name}: {self.short_position}"

    class Meta:
        verbose_name = _("Персонал")
        verbose_name_plural = _("Персонал")


class AdditionalData(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Дополнительная информация персонала")
        verbose_name_plural = _("Дополнительные информации персонала")


class StaffAdditionalData(models.Model):
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="additionals"
    )
    additional_data = models.ForeignKey(
        AdditionalData, on_delete=models.CASCADE, related_name="additionals"
    )
    content = models.TextField()

    class Meta:
        verbose_name = _("Дополнительная информация")
        verbose_name_plural = _("Дополнительная информация")


class Vacancy(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ru.title} | {self.en.title} | {self.kg.title}"

    class Meta:
        verbose_name = _("Вакансия")
        verbose_name_plural = _("Вакансии")


class VacancyAbstract(models.Model):
    parent = NotImplemented
    title = models.CharField(max_length=255)
    body = models.TextField()
    salary = models.CharField(max_length=255)

    @classmethod
    def get_serializer(cls):
        class GenericSerializer(serializers.ModelSerializer):
            class Meta:
                model = cls
                fields = ['title', 'body', 'salary']
                ref_name = cls.__class__.__name__

        return GenericSerializer(read_only=True)

    class Meta:
        abstract = True


class VacancyRU(VacancyAbstract):
    parent = models.OneToOneField(Vacancy, on_delete=models.CASCADE, related_name='ru')


class VacancyEN(VacancyAbstract):
    parent = models.OneToOneField(Vacancy, on_delete=models.CASCADE, related_name='en')


class VacancyKG(VacancyAbstract):
    parent = models.OneToOneField(Vacancy, on_delete=models.CASCADE, related_name='kg')
