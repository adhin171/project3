from django import forms
from . models import market

class MarketForm(forms.ModelForm):
    class Meta:
        model=market
        fields=['name','desc','year','img']

