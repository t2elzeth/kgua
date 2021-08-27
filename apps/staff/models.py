from django.db import models

from utils.models import MultilanguageModel, AbstractModelWithGenericSerializer
from django.utils.translation import gettext as _


class Staff(MultilanguageModel):
    date_created = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(
        "department.Department",
        on_delete=models.CASCADE,
        related_name="teachers",
    )

    repr_key = "full_name"

    class Meta:
        verbose_name = _("Преподователь")
        verbose_name_plural = _("Преподователи")


class StaffContacts(models.Model):
    staff = models.OneToOneField(
        "Staff", on_delete=models.CASCADE, related_name="contacts"
    )
    phone = models.CharField(max_length=255)


class StaffContactEmail(models.Model):
    contact = models.OneToOneField(
        "StaffContacts", on_delete=models.CASCADE, related_name="email"
    )
    corporate = models.EmailField()
    personal = models.EmailField()


class StaffExperience(models.Model):
    staff = models.OneToOneField(
        "Staff", on_delete=models.CASCADE, related_name="experience"
    )
    overall = models.IntegerField()
    pedagogical = models.IntegerField()


class StaffEducation(models.Model):
    staff = models.ForeignKey(
        "Staff", on_delete=models.CASCADE, related_name="education"
    )
    from_year = models.IntegerField()
    to_year = models.IntegerField()
    description = models.TextField()


class StaffAbstract(AbstractModelWithGenericSerializer):
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    fields = ["full_name", "role"]

    class Meta:
        abstract = True


class StaffRU(StaffAbstract):
    parent = models.OneToOneField(
        Staff, on_delete=models.CASCADE, related_name="ru"
    )


class StaffEN(StaffAbstract):
    parent = models.OneToOneField(
        Staff, on_delete=models.CASCADE, related_name="en"
    )


class StaffKG(StaffAbstract):
    parent = models.OneToOneField(
        Staff, on_delete=models.CASCADE, related_name="kg"
    )
