from django.db import models


class InternationalEvent(models.Model):
    date_from = models.DateField()
    date_to = models.DateField()

    title = models.CharField(max_length=512)
    description = models.TextField()

    def __str__(self):
        return f"InternationalEvent {self.title}: {self.date_from}-{self.date_to}"

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class InternationalEventImage(models.Model):
    InternationalEvent = models.ForeignKey(
        InternationalEvent, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField()

    def __str__(self):
        return f"Image #{self.id} of {self.InternationalEvent}"

    class Meta:
        verbose_name = 'Картинка мероприятия'
        verbose_name_plural = 'Картинки мероприятия'
