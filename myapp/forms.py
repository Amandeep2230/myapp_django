from django import forms
from .models import Order
from django.core.validators import MinValueValidator
from django.core.validators import MinValueValidator
from .models import Order


class InterestForm(forms.Form):
    CHOICES = [
        (1, "Yes"),
        (0, "No")
    ]
    interested = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    levels = forms.IntegerField(widget=forms.NumberInput, initial=1, validators=[MinValueValidator(1)])
    comments = forms.CharField(widget=forms.Textarea, label='Additional Comments', required=False)


# Lab 8 - Order Model Form
class OrderForm(forms.ModelForm):
    levels = forms.IntegerField(widget=forms.NumberInput, initial=1, validators=[MinValueValidator(1)])

    class Meta:
        model = Order
        fields = ['student', 'course', 'levels', 'order_date']
        # Set widgets
        widgets = {
            'student': forms.RadioSelect(),
            'order_date': forms.SelectDateWidget(),
        }