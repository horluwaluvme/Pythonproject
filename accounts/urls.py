#url files for account and it must contain every linkable pages that can be access from accounts
from django.urls import path
from .views import signup, login, forgetpassword


urlpatterns = [
    path("signup/", signup),
    path("login/", login),
    path("forget-password/", forgetpassword)
    
    
    
]
