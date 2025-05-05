from django.shortcuts import render, HttpResponse

from .forms import postt

# Create your views here.

# def home(request):
#     return HttpResponse("Hello USA")


def home(request):
    fm = postt()
    return render(request, 'home.html',{"form":fm})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def sign_up(request):
    return render(request, 'signup.html')