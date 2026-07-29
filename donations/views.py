from django.shortcuts import render,redirect ,get_object_or_404

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Donation

from campaigns.models import Campaign
from .forms import DonationForm

@login_required
def donate(request,id):
    campaign=get_object_or_404(
        Campaign,
        id=id,
        status="APPROVED"
    )
    if request.method=="POST":
        form=DonationForm(request.POST)
        if form.is_valid():
            donation=form.save(commit=False)
            donation.donor=request.user
            donation.campaign=campaign
            
            donation.save()
            
            campaign.raised_amount+=donation.amount
            campaign.save()
            
            return redirect("campaign_detail",id=campaign.id)
    else:
        form=DonationForm()
    
    return render(
        request,
        "donations/donate.html",
        {
            "campaign":campaign,
            "form":form
        }
    )

@login_required
def my_donations(request):
    donations=Donation.objects.filter(
        donor=request.user
    )
    return render(
        request,
        "donations/my_donations.html",
        {
            "donations":donations
        }
    )
        