from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contacts.html")

#def join (request):
#    return HttpResponse("<h1> Join us </hi>")
