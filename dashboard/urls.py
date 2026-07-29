from django.urls import path
from . import views

urlpatterns = [

    path(
        "donor/",
        views.donor_dashboard,
        name="donor_dashboard"
    ),

    path(
        "ngo/",
        views.ngo_dashboard,
        name="ngo_dashboard"
    ),

]