from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import CampaignForm
from .models import Campaign
from django.http import HttpResponseForbidden

@login_required
def create_campaign(request):

    if request.method == "POST":

        form = CampaignForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            campaign = form.save(
                commit=False
            )

            campaign.ngo = request.user

            campaign.save()

            return redirect(
                "ngo_dashboard"
            )

    else:

        form = CampaignForm()


    return render(
        request,
        "campaigns/create_campaign.html",
        {
            "form": form
        }
    )


# This show single campaign in details
def campaign_detail(request,id):
    campaign=get_object_or_404(
        Campaign,
        id=id,
        status="APPROVED"
    )
    return render(
        request,
        "campaigns/detail.html",
        {
            "campaign":campaign
        }
    )
    
    
@login_required
def my_campaigns(request):
    if request.user.role !="NGO":
        return HttpResponseForbidden("Access Denied!.")
    campaigns=Campaign.objects.filter(
        ngo=request.user
    )
    return render(
        request,
        "campaigns/my_campaigns.html",
        {
            "campaigns":campaigns
        }
    )