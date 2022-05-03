from django import forms
from .models import Payments

class PaymentForms(forms.Form):
    class Meta:
        model = Payments