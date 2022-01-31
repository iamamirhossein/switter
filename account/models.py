from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance, )
        profile.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True,
    )
    bio = models.TextField(blank=True)
    is_private = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(null=True, upload_to='img/profiles/')

    def __str__(self):
        return self.user.username

    @property
    def complete_name(self):
        return self.user.first_name + ' ' + self.user.last_name
