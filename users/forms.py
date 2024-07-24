from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField

from .models import User
from products.models import Product


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'skin_type')


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={
            'autocomplete': 'off',
            'autofocus': True,
            'value': '',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'off',
            'value': '',
            'placeholder': 'Password'
        }),
    )


class UserUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('username', 'email', 'skin_type')


class UserDeleteForm(forms.Form):
    confirm = forms.BooleanField(label="I confirm that I want to delete my account")

