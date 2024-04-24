from django import forms
from .models import Seller
from lands.models import Land


class LandUploadForm(forms.ModelForm):
    class Meta:
        model = Land
        fields = ['location', 'size', 'price', 'description', 'images', 'document']


class SellerAgreementForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['full_name', 'house_address', 'state', 'phone_number', 'profile_image']

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'house_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your house address'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your state'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
