from django import forms
from .models import Pay

class PaymentForms(forms.Form):
    class Meta:
        model = Payments