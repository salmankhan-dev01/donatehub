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
    ),
    path(
        "delete<int:id>/",
        views.delete_campaign,
        name="delete_campaign"
    ),
    path(
        "edit/<int:id>/",
        views.edit_campaign,
        name="edit_campaign"
    )
]