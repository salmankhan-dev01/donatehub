from django.contrib import admin
from .models import Campaign


@admin.action(description="Approve select campaigns")
def approve_campaigns(modeladmin,request,queryset):
    queryset.update(
        status="APPROVED"
    )

@admin.action(description="Reject Selected campaings")
def reject_campaigns(modelmin,request,queryset):
    queryset.update(
        status="REJECTED"
    )

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "ngo",
        "category",
        "goal_amount",
        "raised_amount",
        "status",
    ]
    
    list_filter = [
        "category",
        "status",
    ]
    actions=[
        approve_campaigns,
        reject_campaigns
    ]