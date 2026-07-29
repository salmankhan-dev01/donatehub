from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def donor_dashboard(request):

    return render(
        request,
        "dashboard/donor_dashboard.html"
    )


@login_required
def ngo_dashboard(request):

    return render(
        request,
        "dashboard/ngo_dashboard.html"
    )