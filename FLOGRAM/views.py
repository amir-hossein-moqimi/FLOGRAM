from urllib import request
import django
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def Media(request):
    return render(request, 'media.html')