from django import forms
from django.core.exceptions import ValidationError


class ExampleForm(forms.Form):
    
    name = forms.CharField(label="your name", max_length=255 , required=True)
    email = forms.EmailField(label="your email", max_length=255, required=True)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'},format="d-m-Y"), input_formats="d-m-Y")
    