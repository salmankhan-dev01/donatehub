from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/",
         views.donate,
         name="donate"
         ),
    path(
        "my/",
        views.my_donations,
        name="my_donations"
    )
]