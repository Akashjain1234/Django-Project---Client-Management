from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control input-lg'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control input-lg'}))

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control input-lg'}),
            'email':forms.EmailInput(attrs={'class':'form-control input-lg'}),
        }