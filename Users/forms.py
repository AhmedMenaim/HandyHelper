from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.contrib.auth import authenticate
from HandyHelperDjango import models
from Users.models import Users

# class LowerField(forms.CharField):
#     def to_python(self, value):
#         return value.lower()

class RegisterationForm(UserCreationForm):
    email               = forms.CharField(max_length=60, help_text='Required. Add a valid email address', label="Email")
    username            = forms.CharField(max_length = 30, help_text='Required. Add a valid username', label="Username")
    firstName           = forms.CharField(max_length = 30,help_text='Required.', label="First Name")
    lastName            = forms.CharField(max_length = 30, help_text='Required.', label="Last Name")

    
    class Meta:
        model = Users
        fields = ("email", "username", "firstName", "lastName", "password1", "password2")

    def clean_username(self):
        return self.cleaned_data['username'].lower()


class UserAuthenticationForm(forms.ModelForm):
    email = forms.CharField(max_length=60, label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")
        