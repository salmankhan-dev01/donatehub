from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from campaigns.models import Campaign

def home(request):
    campaigns=Campaign.objects.filter(
        status="APPROVED"
    )
    return render(
        request,
        "core/home.html",
        {
            "campaigns":campaigns
        }
    )