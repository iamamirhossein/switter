from django.db import models
from django.contrib.auth.models import User


class SweetManager(models.Manager):

    def published(self):
        return self.filter(draft=False).order_by('-created_at')


class Sweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sweets')
    body = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    draft = models.BooleanField(default=False)
    re_sweet = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'sweet'
        verbose_name_plural = 'sweets'

    def __str__(self):
        return self.body[:45]

    @property
    def faves_count(self):
        return self.faves.count()

    objects = SweetManager()


class Fave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='faves')
    sweet = models.ForeignKey(Sweet, on_delete=models.CASCADE, related_name='faves')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + self.sweet.body[:30]
