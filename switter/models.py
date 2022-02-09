from django.db import models
from django.contrib.auth.models import User


class Sweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sweets')
    body = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    draft = models.BooleanField(default=False)
    re_sweet = models.BooleanField(default=True)


class Fave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='faves')
    sweet = models.ForeignKey(Sweet, on_delete=models.CASCADE, related_name='faves')
    created_at = models.DateTimeField(auto_now_add=True)
