import os

from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Staff


@receiver(pre_save, sender=Staff)
def compress_image(instance, **kwargs):
    print("Signal is working")

    previous = Staff.objects.filter(id=instance.id).first()

    if previous is not None and instance.image is not None and previous.image != instance.image:
        print("Image has changed")
        os.popen(f"mogrify -resize 1000x1000^ -gravity center -extent 1000x1000 -quality 75 {os.path.join(settings.MEDIA_ROOT, instance.image.name)}")
