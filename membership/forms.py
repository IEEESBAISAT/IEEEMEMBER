from django import forms
from .models import data1, ADM
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Textarea, ChoiceField


class NameForm(forms.ModelForm):
    class Meta:
        model = data1
        fields = ('name', 'email', 'contact', 'branch', 'year')
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 200px;',
                'placeholder': 'name'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 200px;',
                'placeholder': 'user@gmail.com etc'
            }),
            'contact': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 200px;',
                'placeholder': 'Mobile'
            }),
            'branch': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 200px;',

            }),
            'year': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 200px;',

            }),

        }


class adlog(forms.ModelForm):
    class Meta:
        model = ADM
        fields = ('adname', 'adpass', 'mdses')
        widgets = {
            'adname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 200px;',
                'placeholder': 'name'
            }),
            'adpass': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 200px;',
                'placeholder': 'pass'
            }),
            'mdses': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 200px;',
                'placeholder': 'set/reset'
            }),
        }
