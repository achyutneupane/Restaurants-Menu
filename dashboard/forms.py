from django import forms
from menu import models


class MenuForm(forms.ModelForm):
    class Meta:
        model = models.MainMenu
        fields = ['name', 'title', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class menuItemsForm(forms.ModelForm):
    class Meta:
        model = models.MenuItems
        fields = ['title', 'main_menu', 'image', 'description', 'price']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'main_menu': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
