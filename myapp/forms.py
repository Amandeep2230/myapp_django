from django import forms
from django.core.validators import MinValueValidator
from .models import Order


class InterestForm(forms.Form):
    CHOICES = [
        ("Yes", 1),
        ("No", 0)
    ]
    interested = forms.ChoiceField(widgets=forms.RadioSelect, choices=CHOICES)
    levels = forms.IntegerField(widget=forms.NumberInput, initial=1, validators=[MinValueValidator(1)])
    comments = forms.CharField(widget=forms.Textarea, label='Additional Comments', blank=True)
