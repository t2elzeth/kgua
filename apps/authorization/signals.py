from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User


@receiver(post_save, sender=User)
def create_profile_if_not_exists(instance, created, **kwargs):
    if created:
        print('New user created and signal worked')
