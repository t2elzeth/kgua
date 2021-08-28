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

    class Meta:
        verbose_name = 'Контакты'


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
        verbose_name = 'Стаж'


class StaffEducation(MultilanguageModel):
    staff = models.ForeignKey(
        "Staff", on_delete=models.CASCADE, related_name="education"
    )
    from_year = models.IntegerField(verbose_name="Начиная с")
    to_year = models.IntegerField(verbose_name="До")

    def __str__(self):
        return f"Edu: of {self.staff} {self.from_year}-{self.to_year}"

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'


class StaffEducationAbstract(AbstractModelWithGenericSerializer):
    description = models.TextField()

    fields = ['description']

    class Meta:
        abstract = True


class StaffEducationRU(StaffEducationAbstract):
    parent = models.OneToOneField(
        StaffEducation, on_delete=models.CASCADE, related_name="ru"
    )


class StaffEducationEN(StaffEducationAbstract):
    parent = models.OneToOneField(
        StaffEducation, on_delete=models.CASCADE, related_name="en"
    )


class StaffEducationKG(StaffEducationAbstract):
    parent = models.OneToOneField(
        StaffEducation, on_delete=models.CASCADE, related_name="kg"
    )


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

    class Meta:
        verbose_name = 'Информация о преподователе на русском'


class StaffEN(StaffAbstract):
    parent = models.OneToOneField(
        Staff, on_delete=models.CASCADE, related_name="en"
    )

    class Meta:
        verbose_name = 'Информация о преподователе на английском'


class StaffKG(StaffAbstract):
    parent = models.OneToOneField(
        Staff, on_delete=models.CASCADE, related_name="kg"
    )

    class Meta:
        verbose_name = 'Информация о преподователе на кыргызском'


class StaffTraining(MultilanguageModel):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='trainings')
    from_year = models.IntegerField(verbose_name="Начиная с")
    to_year = models.IntegerField(verbose_name="До")

    def __str__(self):
        return f"Edu: of {self.staff} {self.from_year}-{self.to_year}"

    class Meta:
        verbose_name = 'Повышение квалификации'
        verbose_name_plural = 'Повышения квалификации'


class StaffTrainingAbstract(AbstractModelWithGenericSerializer):
    description = models.TextField()

    fields = ['description']

    class Meta:
        abstract = True


class StaffTrainingRU(StaffTrainingAbstract):
    parent = models.OneToOneField(
        StaffTraining, on_delete=models.CASCADE, related_name="ru"
    )


class StaffTrainingEN(StaffTrainingAbstract):
    parent = models.OneToOneField(
        StaffTraining, on_delete=models.CASCADE, related_name="en"
    )


class StaffTrainingKG(StaffTrainingAbstract):
    parent = models.OneToOneField(
        StaffTraining, on_delete=models.CASCADE, related_name="kg"
    )



class StaffScientificWorks(MultilanguageModel):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='scientific_works')
    release_date = models.DateField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"SciWork: of {self.staff} {self.release_date}"

    class Meta:
        verbose_name = 'Научный труд'
        verbose_name_plural = 'Научные труды'


class StaffScientificWorksAbstract(AbstractModelWithGenericSerializer):
    title = models.CharField(max_length=512)
    magazin_name = models.CharField(max_length=512)

    fields = ['title', 'magazin_name']

    class Meta:
        abstract = True


class StaffScientificWorksRU(StaffScientificWorksAbstract):
    parent = models.OneToOneField(
        StaffScientificWorks, on_delete=models.CASCADE, related_name="ru"
    )


class StaffScientificWorksEN(StaffScientificWorksAbstract):
    parent = models.OneToOneField(
        StaffScientificWorks, on_delete=models.CASCADE, related_name="en"
    )


class StaffScientificWorksKG(StaffScientificWorksAbstract):
    parent = models.OneToOneField(
        StaffScientificWorks, on_delete=models.CASCADE, related_name="kg"
    )

