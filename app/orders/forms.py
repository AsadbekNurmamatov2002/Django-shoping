from django import forms
from .models import Order
class OrderCreateForm(forms.ModelForm):
    first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiya'}))
    last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ism'}))
    email=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    address=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manzil'}))
    postal_code=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Poshta'}))
    city=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shahar'}))
    telefon=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'telefon raqam'}))
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address','postal_code', 'city']