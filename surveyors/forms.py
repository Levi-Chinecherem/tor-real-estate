# forms.py in the Surveyors app

from django import forms
from .models import Surveyor

class SurveyorApplicationForm(forms.ModelForm):
    class Meta:
        model = Surveyor
        fields = ['full_name', 'house_address', 'state', 'phone_number', 'image', 'resume']

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2 w-full'}),
            'house_address': forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2 w-full'}),
            'state': forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2 w-full'}),
            'phone_number': forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2 w-full'}),
            'image': forms.FileInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2 w-full'}),
            'resume': forms.FileInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2 w-full'}),
        }
