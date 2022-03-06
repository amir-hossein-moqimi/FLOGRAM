from ast import If
from django.shortcuts import render,redirect
from . import forms,models
# Create your views here.
def login(request):
    return render(request, 'login.html')
def signup(request):
    # print(request.POST)
    if request.method == 'POST':
        form = forms.CreationForm(request.POST)
        if form.is_valid():
            print("--------------------------------")
            #not validated completely
            ins = form.save(commit=False)
            ins.username = request.POST.get('Username')
            ins.Instagram = request.POST.get('Instagram')
            ins.password = request.POST.get('Password')
            ins.email = request.POST.get('Email')
            ins.save()
    else:
        form = forms.CreationForm()
    return render(request, 'signup.html')