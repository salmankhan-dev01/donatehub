from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import CampaignForm
from .models import Campaign
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from .forms import CampaignUpdateForm

@login_required
def create_campaign(request):
    
    if request.user.role != "NGO":
        return redirect("home")
    
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
        status__in=["APPROVED","COMPLETED"]
    )
    remaining_amount = campaign.goal_amount - campaign.raised_amount
    return render(
        request,
        "campaigns/detail.html",
        {
            "campaign":campaign,
            "remaining_amount":remaining_amount
        } 
    )
    
    
@login_required
def my_campaigns(request):
    if request.user.role !="NGO":
        return redirect("home")
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
    
@login_required
def delete_campaign(request,id):
    campaign=get_object_or_404(
        Campaign,
        id=id,
        ngo=request.user
    )
    if request.method == "POST":
        campaign.delete()
        return redirect("my_campaigns")
    return redirect("my_campaigns")

@login_required
def edit_campaign(request,id):
    campaign=get_object_or_404(
        Campaign,
        id=id,
        ngo=request.user
    )
    
    if request.method == "POST":
        form=CampaignUpdateForm(request.POST, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect("my_campaigns")
    else:
        form=CampaignUpdateForm(instance=campaign)
    return render(
        request,
        "campaigns/edit_campaign.html",
        {
            "form":form
        }
    )