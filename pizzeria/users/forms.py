from django import forms

class RegisterForm(forms.Form):

    username = forms.CharField(label='Username', max_length=100)
    firstname = forms.CharField(label='First name', max_length=100)
    lastname = forms.CharField(label='Last name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    password_again = forms.CharField(label='And again..', max_length=100, widget=forms.PasswordInput)

from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'password']
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
