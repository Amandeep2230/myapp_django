from django import forms
<<<<<<< HEAD
from .models import Order
from django.core.validators import MinValueValidator
=======
from django.core.validators import MinValueValidator
from .models import Order
>>>>>>> 290c1128560543449f6500c4cb0b2ea2960667db


class InterestForm(forms.Form):
    CHOICES = [
        (1, "Yes"),
        (0, "No")
    ]
<<<<<<< HEAD
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
=======
    interested = forms.ChoiceField(widgets=forms.RadioSelect, choices=CHOICES)
    levels = forms.IntegerField(widget=forms.NumberInput, initial=1, validators=[MinValueValidator(1)])
    comments = forms.CharField(widget=forms.Textarea, label='Additional Comments', blank=True)
>>>>>>> 290c1128560543449f6500c4cb0b2ea2960667db
