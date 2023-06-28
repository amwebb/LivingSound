from django import forms
from .models import GardenEntry

class GardenForm(forms.ModelForm):

    class Meta:
        model = GardenEntry
        fields = ['picture', 'sound', 'rating', 'message']
        exclude = ("username", )
        widgets = {
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
            'sound': forms.FileInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'}),
        }