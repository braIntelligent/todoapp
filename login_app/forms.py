from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        label='nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=50,
        label='contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )