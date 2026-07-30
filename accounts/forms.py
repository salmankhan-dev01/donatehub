from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "phone",
            "role",
            "password1",
            "password2",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control"
            })
        self.fields["role"].widget.attrs["class"] = "form-select"
        
        self.fields["first_name"].required = True
        self.fields["username"].required = True
        self.fields["email"].required = True
        self.fields["role"].required = True
        self.fields["password1"].required = True
        self.fields["password2"].required = True
        
        
        
        self.fields["first_name"].error_messages = {
            "required": "First Name is Required."
        }
        
        self.fields["username"].error_messages = {
                    "required": "Username is Required."
        }
        
        self.fields["email"].error_messages = {
            "required": "Email is Required."
        }
        
        self.fields["role"].error_messages = {
            "required": "Role is Required."
        }
        
        self.fields["password1"].error_messages = {
            "required": "Password is Required."
        }
        
        self.fields["password2"].error_messages = {
            "required": "Confirm Password is Required."
        }