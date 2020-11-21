from django.forms import ModelForm
from django import forms
from .models import *

class clientForm(forms.ModelForm):
    class Meta:
        model   = client
        fields  = ['name','surname','phone','email','price']
        widgets = {

            'name':forms.TextInput(attrs={'class':'form__field','id':'name','name':'name','placeholder':'name','maxlength':'"20"'}),
            'surname':forms.TextInput(attrs={'class':'form__field','id':'surname','surname':'surname','placeholder':'surname','maxlength':'"30"'}),
            'phone':forms.TextInput(attrs={'class':'form__field','id':'surname','phone':'phone','placeholder':'phone','maxlength':'"10"'}),
            'email':forms.TextInput(attrs={'class':'form__field','id':'surname','email':'email','placeholder':'email','maxlength':'"40"'}),
            'price':forms.TextInput(attrs={})

        }
