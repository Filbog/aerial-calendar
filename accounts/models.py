# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Add any custom fields here
    email = models.EmailField(unique=True)
    alias = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.email
