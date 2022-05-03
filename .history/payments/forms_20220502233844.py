from django import forms


class PaymentForms(forms.Form):
    class Meta:
        model = 