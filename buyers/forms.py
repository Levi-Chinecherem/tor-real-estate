from django import forms
from .models import Buyer

class BuyerAgreementForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['full_name', 'house_address', 'state', 'phone_number']
        labels = {
            'full_name': 'Full Name',
            'house_address': 'House Address',
            'state': 'State',
            'phone_number': 'Phone Number'
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2 w-full'}),
            'house_address': forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2 w-full'}),
            'state': forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2 w-full'}),
            'phone_number': forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2 w-full'}),
        }
