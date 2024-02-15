from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    This is a customized version of the
    in built AbstractUser model that came with
    django.
    """
    age = models.PositiveIntegerField(null=True, blank=True)

