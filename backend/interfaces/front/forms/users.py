from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from apps.users.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=30, label='Password', widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'})
    )
    username = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat password'}),
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class VerifyEmailForm(forms.Form):
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        disabled=True,
        required=False,
    )
    code = forms.CharField(
        label='Enter the confirmation code',
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirmation code'}),
    )

    def clean_code(self):
        code = self.cleaned_data['code']
        for elem in code:
            if not elem.isdigit():
                raise ValidationError('Only digits are allowed')
        return code
