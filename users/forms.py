from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'phone_number', 'full_name', 'avatar', )


class ResetPasswordForm(forms.Form):

    email = forms.EmailField()
