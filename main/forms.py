from django import forms
from .models import Bottle

class BottleForm(forms.ModelForm):
    class Meta:
        model = Bottle
        fields = ['name', 'full_weight', 'empty_weight', 'full_volume', 'liquid_density',]
class CalculateRemainingForm(forms.Form):
    current_weight = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        label='Текущий вес бутылки (в граммах)',
        widget=forms.NumberInput(attrs={'placeholder': 'Введите текущий вес бутылки'})
    )