from django.db import models
from django.utils.translation import gettext as _
from utils.models import CompressImageBeforeUpload
import sys
from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


class Staff(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(
        "department.Department",
        on_delete=models.CASCADE,
        related_name="teachers",
    )
    full_name = models.CharField(max_length=512)
    image = models.ImageField(blank=True, null=True)

    position = models.CharField(max_length=512)

    class Meta:
        verbose_name = _("Преподаватель")
        verbose_name_plural = _("Преподаватели")

    def __str__(self):
        return f"{self.full_name}: {self.position}"


class StaffContacts(models.Model):
    staff = models.OneToOneField(
        "Staff", on_delete=models.CASCADE, related_name="contacts"
    )
    phone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Контакты"


class StaffContactEmail(models.Model):
    contact = models.OneToOneField(
        "StaffContacts", on_delete=models.CASCADE, related_name="email"
    )
    corporate = models.EmailField(blank=True, null=True)
    personal = models.EmailField(blank=True, null=True)


class StaffExperience(models.Model):
    staff = models.OneToOneField(
        "Staff", on_delete=models.CASCADE, related_name="experience"
    )
    overall = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pedagogical = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = "Стаж"


class StaffEducation(models.Model):
    staff = models.ForeignKey(
        "Staff", on_delete=models.CASCADE, related_name="education"
    )
    from_year = models.IntegerField(verbose_name="Начиная с", blank=True, null=True)
    to_year = models.IntegerField(verbose_name="До", blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        # return f"Edu: of {self.staff} {self.from_year}-{self.to_year}"
        return f"#{self.id}"

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образования"


class StaffTraining(models.Model):
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="trainings"
    )
    date = models.CharField(max_length=512, verbose_name="Дата", blank=True, null=True)
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"Edu: of {self.staff} {self.date}"

    class Meta:
        verbose_name = "Повышение квалификации"
        verbose_name_plural = "Повышения квалификации"


class StaffScientificWorks(models.Model):
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="scientific_works"
    )
    release_date = models.CharField(max_length=512, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=512)
    magazin_name = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return f"SciWork: of {self.staff} {self.release_date}"

    class Meta:
        verbose_name = "Научный труд"
        verbose_name_plural = "Научные труды"


class StaffReward(models.Model):
    department = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="rewards"
    )
    date = models.CharField(max_length=512, verbose_name="Дата получения", blank=True, null=True)
    description = models.TextField(verbose_name="Информация о награде")
