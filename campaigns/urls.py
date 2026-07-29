from django.urls import path
from . import views


urlpatterns = [

    path(
        "create/",
        views.create_campaign,
        name="create_campaign"
    ),
    path(
        "<int:id>/",
        views.campaign_detail,
        name="campaign_detail"
    ),
    path(
        "my/",
        views.my_campaigns,
        name="my_campaigns"
    )
]