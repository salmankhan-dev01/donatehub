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
        ]
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        if "description" in self.fields:
            self.fields["description"].widget.attrs["rows"] = 5
        self.fields["category"].widget.attrs["class"] = "form-select"
        
        
        self.fields["title"].error_messages = {
            "required": "Title is required."
        }

        self.fields["description"].error_messages = {
            "required": "Description is required."
        }

        self.fields["category"].error_messages = {
            "required": "Category is required."
        }

        self.fields["goal_amount"].error_messages = {
            "required": "Goal Amount is required."
        }
    def clean_title(self):
        title=self.cleaned_data.get("title")
        if not title or not title.strip():
            raise forms.ValidationError("Title is required")
        return title
    def clean_description(self):
            description=self.cleaned_data.get("description")
            if not description or not description.strip():
                raise forms.ValidationError("Description is required")
            return description
    def clean_goal_amount(self):
        amount=self.cleaned_data.get("goal_amount")
        
        if amount is None or amount<=0:
            raise forms.ValidationError("Goal Amount must be greater than 0.")
        return amount


class CampaignUpdateForm(forms.ModelForm):
    class Meta:
        model=Campaign
        fields=[
            "title",
            "description",
            "category"
        ]
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields["title"].widget.attrs["class"] = "form-control"
        self.fields["description"].widget.attrs["class"] = "form-control"
        self.fields["category"].widget.attrs["class"] = "form-select"
        
        self.fields["title"].error_messages={
            "required":"Title is required."
        }
        self.fields["description"].error_messages={
            "required":"Description is required."
        }
        self.fields["category"].error_messages={
            "required":"Category is required."
        }
            