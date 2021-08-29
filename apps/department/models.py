from django.db import models

from utils.models import MultilanguageModel, AbstractModelWithGenericSerializer
from django.utils.translation import gettext as _


class Department(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=512)
    foundation_year = models.IntegerField(verbose_name='Год образования')
    pps_number = models.TextField(verbose_name='Количество преподователей')
    activities = models.TextField(verbose_name='Деятельность кафедры')
    pps_info = models.TextField(verbose_name='Информация о ППС')

    description = models.TextField(verbose_name='Информация о кафедре')

    class Meta:
        verbose_name = _("Кафедра")
        verbose_name_plural = _("Кафедры")

    def __str__(self):
        return f"{self.title_ru} | {self.title_en} | {self.title_ky}"


class DepartmentHeadTeacher(models.Model):
    department = models.OneToOneField(Department, on_delete=models.CASCADE, related_name='head_teacher')
    teacher = models.ForeignKey('staff.Staff', on_delete=models.CASCADE, related_name='head_teacher',
                                verbose_name='Зав.кафедры')

    class Meta:
        verbose_name = 'Заведующий'


class DepartmentContacts(models.Model):
    department = models.OneToOneField(Department, on_delete=models.CASCADE, related_name='contacts')
    phone = models.CharField(max_length=255)
    first_email = models.EmailField()
    second_email = models.EmailField(blank=True, null=True)


class DepartmentReward(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='rewards')
    year = models.IntegerField(verbose_name='Год получения')
    description = models.TextField(verbose_name='Информация о награде')
