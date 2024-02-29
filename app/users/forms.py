from django import forms
from .models import User, Profile
from django.contrib.auth.forms import PasswordResetForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Invisible, ReCaptchaV2Checkbox

from django.contrib.auth.forms import SetPasswordForm

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['password', 'password2']
  
class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")
    # captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
    class Meta:
        model=User
        fields=['email','first_name','last_name']
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
class UserLogin(forms.Form):
    email=forms.EmailField(max_length=250, widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Username or Email")
    password=forms.CharField(max_length=15, widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Parol")
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox) 

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']