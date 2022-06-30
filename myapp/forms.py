from django import forms
from myapp.models import Order


class InterestForm(forms.Form):
    CHOICES = [
        ("Yes", 1),
        ("No", 0)
    ]
    interested = forms.ChoiceField(widgets=forms.RadioSelect, choices=CHOICES)
    levels = forms.IntegerField(widget=forms.NumberInput, initial=1)
    comments = forms.CharField(widget=forms.Textarea, label='Additional Comments')



