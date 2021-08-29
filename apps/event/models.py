from django.db import models


class Event(models.Model):
    date_from = models.DateField()
    date_to = models.DateField()

    title = models.CharField(max_length=512)
    description = models.TextField()

    def __str__(self):
        return f"Event {self.title}: {self.date_from}-{self.date_to}"


class EventImage(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField()

    def __str__(self):
        return f"Image #{self.id} of {self.event}"
