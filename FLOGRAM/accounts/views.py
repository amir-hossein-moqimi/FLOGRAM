from django.shortcuts import render
# Create your views here.
def login(request):
    render(request, 'login.html')
def signup(request):
    render(request, 'signup.html')