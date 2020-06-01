from django import forms
from .models import Customers
#from django.core.validators import CharField

class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length =45)
    email = forms.EmailField()
    
    def clean_email(self):
        em = self.cleaned_data['email']
        if Customers.objects.filter(email = em).count() > 0:
            raise forms.ValidationError(" email already used try another one")
        return em


class Booking_id(forms.Form):
    Booking_id = forms.IntegerField(label = "booking_id")