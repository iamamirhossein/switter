from django.db import models
from django.contrib.auth.models import User


class Sweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sweets')
    body = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    draft = models.BooleanField(default=False)
