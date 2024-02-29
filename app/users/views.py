from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLogin, UserCreateForm


def LoginPage(request):
    if request.method=='POST':
        forms=UserLogin(request.POST)
        if forms.is_valid():
            cd=forms.cleaned_data
            user=authenticate(request,email=cd['email'],password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'yashi')
                return redirect('product:home')
            else:
                messages.debug(request, 'd')
        else:
            messages.error(request, 'e')
    else:
        forms=UserLogin()
    return render(request, 'login/login.html', {})


def RegisterPage(request):
    if request.method=="POST":
        forms=UserCreateForm(request.POST)
        if forms.is_valid():
            user=forms.save(commit=False)
            user.set_password(user.cleaned_data['password'])
            user.save()
    else:
        forms=UserCreateForm()
    return render(request, 'login/login.html', {})


def LogoutPage(request):
    if request.method=='POST':
        logout(request)
        
    return render(request, 'login/login.html', {})

