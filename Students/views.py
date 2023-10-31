from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html' )

def contact(request):
    return render(request, 'contact.html')

def add(request):
    return render(request, 'add.html')   


# def hello(request):
#     return render(request, 'about.h'tml')

# def hello(request):
#     return render(request, 'layout.html')