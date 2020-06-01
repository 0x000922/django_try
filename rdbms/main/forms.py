from django import forms
#from django.core.validators import CharField

class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length =45)
    email = forms.EmailField()


class Booking_id(forms.Form):
    Booking_id = forms.IntegerField(label = "booking_id")