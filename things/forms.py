"""Forms of the project."""
from django import forms
from .models import Thing

# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        exclude = ["created_at"]
        widgets = {
            "description" : forms.Textarea(),
            "quantity" : forms.NumberInput()
        }
    