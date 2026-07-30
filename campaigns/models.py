from django.db import models
from django.conf import settings


class Campaign(models.Model):

    CATEGORY_CHOICES = [
        ("OTHER", "Other"),
        ("MEDICAL", "Medical"),
        ("EDUCATION", "Education"),
        ("FOOD", "Food"),
        ("DISASTER", "Disaster Relief"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
        ("COMPLETED", "Completed"),
    ]


    ngo = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="campaigns"
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="OTHER"
    )

    goal_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    raised_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    image = models.ImageField(
        upload_to="campaigns/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.title