from django import forms
from .models import LoginRecord

class LogiForm(forms.ModelForm):
    class Meta:
        model = LoginRecord
        fields = ['contact', 'password']
        widgets = {
            'contact': forms.TextInput(attrs={'placeholder': 'Email or phone number'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }
