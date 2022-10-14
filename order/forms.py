from django import forms
from .models import Order


class StepTwoForm(forms.ModelForm):
    class Meta:
        model = Order
        widgets = {
            "delivery": forms.RadioSelect(attrs={"class": "toggle-box"}),
            "city": forms.TextInput(attrs={"class": "form-input border-custom"}),
            "address": forms.Textarea(attrs={"class": "form-textarea border-custom"}),
        }
        fields = ["delivery", "city", "address"]


class StepThreeForm(forms.ModelForm):
    class Meta:
        model = Order
        widgets = {
            "payment": forms.RadioSelect(attrs={"class": "toggle-box"}),
        }
        fields = [
            "payment",
        ]
