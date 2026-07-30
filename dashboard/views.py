from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db import models
from campaigns.models import Campaign
from donations.models import Donation
from django.shortcuts import redirect


@login_required
def donor_dashboard(request):
    
    if request.user.role != "DONOR":
        return redirect("ngo_dashboard")
    return render(
        request,
        "dashboard/donor_dashboard.html"
    )


@login_required
def ngo_dashboard(request):
    if request.user.role != "NGO":
        return redirect("donor_dashboard")
    campaigns=Campaign.objects.filter(
        ngo=request.user
    )
    total_campaigns=campaigns.count()
    approved_campaigns=campaigns.filter(
        status="APPROVED"
    ).count()
    pending_campaigns=campaigns.filter(
        status="PENDING"
    ).count()
    total_donations=Donation.objects.filter(
        campaign__ngo=request.user
    ).aggregate(
        total=models.Sum("amount")
    )['total'] or 0
    return render(
        request,
        "dashboard/ngo_dashboard.html",
        {
            "total_campaigns":total_campaigns,
            "approved_campaigns":approved_campaigns,
            "pending_campaigns":pending_campaigns,
            "total_donations":total_donations
        }
    )