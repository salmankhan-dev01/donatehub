from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CampaignForm


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