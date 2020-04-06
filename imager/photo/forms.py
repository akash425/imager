from django import forms

from .models import input
'''
opration_type = (
    ()
)
'''
class upload(forms.Form):
    input_image = forms.ImageField()
    #name = forms.CharField()