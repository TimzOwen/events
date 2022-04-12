from django import forms
from django.forms import ModelForm
from .models import Venue


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Event Venue'}),
            'address': forms.TextInput(attrs={'class': 'form-control','placeholder':'Event Address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control','placeholder':'Event Zip Code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','placeholder':'Organizer Phone number'}),
            'web': forms.TextInput(attrs={'class': 'form-control','placeholder':'Web URL Event'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email to event'}),
        }
