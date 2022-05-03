from django import forms
from .models import Pa

class PaymentForms(forms.Form):
    class Meta:
        model = Payments