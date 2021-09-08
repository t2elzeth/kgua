from django.db import models
from django.utils.translation import gettext as _


class Bureau(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=512)
    activities = models.TextField(verbose_name="Деятельность", blank=True, null=True)
    goal = models.TextField(verbose_name="Цель", blank=True, null=True)
    tasks = models.TextField(verbose_name="Задачи", blank=True, null=True)

    class Meta:
        verbose_name = _("Отдел")
        verbose_name_plural = _("Отделы")

    def __str__(self):
        return f"{self.title_ru} | {self.title_en} | {self.title_ky}"


class BureauContacts(models.Model):
    bureau = models.OneToOneField(
        Bureau, on_delete=models.CASCADE, related_name="contacts"
    )
    phone = models.CharField(max_length=255, blank=True, null=True)
    first_email = models.EmailField(blank=True, null=True)
    second_email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=512, verbose_name="Адрес", blank=True, null=True)


class BureauMember(models.Model):
    bureau = models.ForeignKey(Bureau, on_delete=models.CASCADE, related_name='members')
    member = models.ForeignKey("staff.Staff", on_delete=models.CASCADE, related_name='bureau_members')

    position = models.CharField(max_length=512, blank=True, null=True)
    specialist = models.BooleanField(default=False, verbose_name="Ведущий специалист?")

    def __str__(self):
        return f"#{self.id}"
