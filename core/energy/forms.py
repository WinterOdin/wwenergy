from django.forms import ModelForm
from django import forms
from .models import *

class clientForm(forms.ModelForm):
    class Meta:
        model   = client
        fields  = ['name','surname','phone','email',]
        widgets = {

            'name':forms.TextInput(attrs={'class':'form__field','id':'name','name':'name','placeholder':'name'}),
            'surname':forms.TextInput(attrs={'class':'form__field','id':'surname','surname':'surname','placeholder':'surname'}),
            'phone':forms.TextInput(attrs={'class':'form__field','id':'surname','phone':'phone','placeholder':'phone'}),
            'email':forms.TextInput(attrs={'class':'form__field','id':'surname','email':'email','placeholder':'email'}),


        }
