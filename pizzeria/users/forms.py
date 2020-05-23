from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    # username = forms.CharField(label='Username', max_length=100)
    # first_name = forms.CharField(label='First name', max_length=100)
    # last_name = forms.CharField(label='Last name', max_length=100)
    # email = forms.EmailField(label='Email', max_length=100)
    # password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    # password_again = forms.CharField(label='And again..', max_length=100, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'password']
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
