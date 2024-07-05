from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm,SetPasswordForm,AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        # fields = '__all__'
        


class ChangeInformationsForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']