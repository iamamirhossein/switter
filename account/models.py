from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True,
    )
    bio = models.CharField(blank=True, max_length=300)
    is_private = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(null=True, upload_to='img/profiles/')

    def __str__(self):
        return self.user.username

    @property
    def complete_name(self):
        return self.user.first_name + ' ' + self.user.last_name
