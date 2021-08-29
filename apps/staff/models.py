from django.db import models
from django.utils.translation import gettext as _

from utils.models import MultilanguageModel, AbstractModelWithGenericSerializer


class Staff(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(
        "department.Department",
        on_delete=models.CASCADE,
        related_name="teachers",
    )
    full_name = models.CharField(max_length=512)
    image = models.ImageField(blank=True, null=True)

    POSITION_TEACHER = "teacher"
    POSITION_RECTOR = "rector"
    POSITION_CHOICES = (
        (POSITION_TEACHER, POSITION_TEACHER),
        (POSITION_RECTOR, POSITION_RECTOR),
    )
    position = models.CharField(max_length=512, choices=POSITION_CHOICES)

    class Meta:
        verbose_name = _("Преподователь")
        verbose_name_plural = _("Преподователи")

    def __str__(self):
        return f"{self.full_name}: {self.position}"


class StaffContacts(models.Model):
    staff = models.OneToOneField(
        "Staff", on_delete=models.CASCADE, related_name="contacts"
    )
    phone = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Контакты"


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

    class Meta:
        verbose_name = "Стаж"


class StaffEducation(MultilanguageModel):
    staff = models.ForeignKey(
        "Staff", on_delete=models.CASCADE, related_name="education"
    )
    from_year = models.IntegerField(verbose_name="Начиная с")
    to_year = models.IntegerField(verbose_name="До")
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
    from_year = models.IntegerField(verbose_name="Начиная с")
    to_year = models.IntegerField(verbose_name="До")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"Edu: of {self.staff} {self.from_year}-{self.to_year}"

    class Meta:
        verbose_name = "Повышение квалификации"
        verbose_name_plural = "Повышения квалификации"


class StaffScientificWorks(MultilanguageModel):
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="scientific_works"
    )
    release_date = models.DateField()
    link = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=512)
    magazin_name = models.CharField(max_length=512)

    def __str__(self):
        return f"SciWork: of {self.staff} {self.release_date}"

    class Meta:
        verbose_name = "Научный труд"
        verbose_name_plural = "Научные труды"


class StaffReward(models.Model):
    department = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="rewards"
    )
    year = models.IntegerField(verbose_name="Год получения")
    description = models.TextField(verbose_name="Информация о награде")
