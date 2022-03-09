from urllib import request
import django
from django.shortcuts import render

def about(rquest):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')