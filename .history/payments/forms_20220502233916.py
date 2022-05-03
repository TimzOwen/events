from django import forms
from .models import 

class PaymentForms(forms.Form):
    class Meta:
        model = Payments