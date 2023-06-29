from django import forms
from .models import GardenEntry
from django.forms import Textarea

class GardenForm(forms.ModelForm):

    choices=(
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        )

    rating = forms.ChoiceField(choices=choices)

    class Meta:
        model = GardenEntry
        fields = ['picture', 'sound', 'rating', 'message']
        exclude = ("username", )
        widgets = {
          'message': Textarea(attrs={'rows':10, 'cols':45}),
        }
        