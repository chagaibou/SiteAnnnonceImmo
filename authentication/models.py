from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class User(AbstractUser):
    phoneNumber = models.CharField(
    max_length=16,
    blank=True,
    null=True,
    validators=[
      RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
      ),
    ],
    )