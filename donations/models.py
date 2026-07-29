from django.db import models

# Create your models here.
from django.conf import settings
from campaigns.models import Campaign


class Donation(models.Model):
    donor=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="donations"
    )
    campaign=models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        related_name="donations"
    )
    amount=models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    donated_at=models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return f"{self.donor.username} donated {self.amount}"