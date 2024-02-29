from django.urls import path  
from django.contrib.auth import views as auth_views
from .views import *

app_name='users'

urlpatterns = [
    path('sigin/',LoginPage, name="sigin"),
    path('signup/', RegisterPage, name="signup"),
    path("signout/",LogoutPage, name="signout"),
]