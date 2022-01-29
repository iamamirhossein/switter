from django.db import models
from django.contrib.auth.models import User


# Create your models here.

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

    def __str__(self):
        return self.user.username
