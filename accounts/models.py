from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    DONOR = "DONOR"
    NGO = "NGO"

    ROLE_CHOICES = [
        (DONOR, "Donor"),
        (NGO, "NGO"),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=DONOR
    )

    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username