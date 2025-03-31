# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # custom fields
    email = models.EmailField(unique=True)
    alias = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        permissions = [
            ("verified", "Can automatically create verified events"),
        ]

    def __str__(self):
        return self.email
