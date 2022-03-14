from ast import If
from distutils import errors
from django.shortcuts import render,redirect
from . import forms,models
# Create your views here.
def login(request):
    return render(request, 'login.html')
def signup(request):
    if request.method == 'POST':
        form = forms.CreationForm(request.POST)
        print(f'request.POST : {request.POST}')
        if form.is_valid():
            #not validated completely
            ins = form.save(commit=False)
            ins.username = request.POST.get('username')
            ins.Instagram = request.POST.get('Instagram')
            ins.password = request.POST.get('password')
            ins.email = request.POST.get('email')
            ins.type = request.POST.get('type')
            ins.save()
            return redirect('accounts:loginpage')
        else:
            print(f'form.errors : {form.errors.as_data()}')
            return render(request, 'signup.html', {'haserror' : True, 'errors' : form.errors})
    else:
        form = forms.CreationForm()
        return render(request, 'signup.html', {'haserror' : False})