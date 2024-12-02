from django import forms

class LogiForm(forms.Form):
    contact = forms.CharField(
        max_length=100,
        label="Email or Phone",
        widget=forms.TextInput(attrs={'placeholder': 'Email or phone number'}),
    )
    password = forms.CharField(
        max_length=100,
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )
