from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def signup(request):
    return render(request, "accounts/signup.html")


def login(request):
    return render(request, "accounts/login.html")

def forgetpassword(request):
    return render(request, "accounts/password.html")
    