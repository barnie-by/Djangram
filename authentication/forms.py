from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from django.forms import TextInput, PasswordInput


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60),

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')

        widgets = {
            'email': forms.TextInput(attrs={
                'style': 'border: 1.25px solid darkgray; border-radius: 10px; height: 35px; width: 220px',
                'placeholder': 'Email',
                'maxlength': 60,

            }),
            'username': TextInput(attrs={
                'style': 'border: 1.25px solid darkgray; border-radius: 10px; height: 35px; width: 220px',
                'placeholder': 'Username',
                'maxlength': 15,
            })
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(
            attrs={
                'style': 'border: 1.25px solid darkgray; border-radius: 10px; height: 35px; width: 220px',
                'placeholder': 'Password'})
        self.fields['password2'].widget = PasswordInput(
            attrs={
                'style': 'border: 1.25px solid darkgray; border-radius: 10px; height: 35px; width: 220px',
                'placeholder': 'Repeat password'})
