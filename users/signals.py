from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)  # when a User is saved with the post_save signal that this function is called
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)  # when a User is saved with the post_save signal than this function is called
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

