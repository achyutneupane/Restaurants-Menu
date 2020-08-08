from django import forms
from . import models

class Contactform(forms.ModelForm):
    class Meta:
        model = models.Contactus
        fields = ['fullname', 'email', 'subject', 'description']

        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control','id':'cf-name', 'name':'name','placeholder':'Full Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control','type': 'email' ,'id':'cf-name','placeholder':'Enter Email', 'name':'name'}),
            'subject': forms.TextInput(attrs={'class': 'form-control','id':'cf-name','placeholder':'Subject', 'name':'name'}),
            'description': forms.Textarea(attrs={'class': 'form-control','rows':'6','id':'cf-name','placeholder':'Tell Me Something', 'name':'name'}),
        }
