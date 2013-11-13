from django.db import models
from django.conf import settings


class Task(models.Model):
    description = models.TextField()
    done = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
