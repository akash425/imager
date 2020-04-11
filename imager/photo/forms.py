from django import forms

from .models import input1
'''
opration_type = (
    (1, 'flip')
)'''
class upload(forms.Form):
    input_image = forms.ImageField()
    #name = forms.CharField()