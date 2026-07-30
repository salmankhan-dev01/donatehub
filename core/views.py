from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from campaigns.models import Campaign

def home(request):
    campaigns=Campaign.objects.filter(
        status__in=["APPROVED", "COMPLETED"]
    )
    return render(
        request,
        "core/home.html",
        {
            "campaigns":campaigns
        }
    )
def custom_404(request,exception):
    return render(request,"404.html",status=404)