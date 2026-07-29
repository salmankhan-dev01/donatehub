from django import forms
from .models import Campaign


class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign

        fields = [
            "title",
            "description",
            "category",
            "goal_amount",
            "image",
        ]