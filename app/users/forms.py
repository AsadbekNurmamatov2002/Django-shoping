from django import forms
from .models import User

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(label='Parol',widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")
    password2 = forms.CharField(label='Parol',widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")
    class Meta:
        model=User
        fields=['email','first_name','last_name']
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
class UserLogin(forms.Form):
    email=forms.EmailField(max_length=250, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")
    password=forms.CharField(max_length=15, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")
