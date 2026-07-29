from django.contrib import admin

# Register your models here.
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = [
        "donor",
        "campaign",
        "amount",
        "donated_at"
    ]