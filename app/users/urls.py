from django.urls import path  
from django.contrib.auth import views as auth_views
from .views import *

app_name='users'

urlpatterns = [
    path('sigin/',LoginPage, name="sigin"),
    path('signup/', RegisterPage, name="signup"),
    path("signout/",LogoutPage, name="signout"),
    path('profile/<str:id>', profile, name='profile'),
    path('edit/',edit, name='edit'),

    path('activate/<uidb64>/<token>/', activate, name='activate'),

    path("password_change/",password_change, name="password_change"),
    path("password_reset/", password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>/', passwordResetConfirm, name='password_reset_confirm'),
]