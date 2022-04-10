from django.shortcuts import render,redirect
from . import forms,models
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    return render(request, 'login.html')
def signup(request):
    # if request.method == 'POST':
    #     form = forms.CreationForm(request.POST)
    #     print(f'request.POST : {request.POST}')
    #     if form.is_valid():
    #         #not validated completely
    #         ins = form.save(commit=False)
    #         ins.username = request.POST.get('username')
    #         ins.Instagram = request.POST.get('Instagram')
    #         ins.password = request.POST.get('password')
    #         ins.email = request.POST.get('email')
    #         ins.type = request.POST.get('type')
    #         ins.save()
    #         return redirect('accounts:loginpage')
    #     else:
    #         print(f'form.errors : {form.errors.as_data()}')
    #         return render(request, 'signup.html', {'haserror' : True, 'errors' : form.errors})
    # else:
    #     form = forms.CreationForm()
    #     return render(request, 'signup.html', {'haserror' : False})
    if request.method == 'POST':
        inputs = request.POST
        print(inputs)
        try:
            #create a 'some fields are empty error'
            username = inputs['username']
            password = inputs['password']
            if password != inputs['Confirm']:
                raise Exception('password missmatch')
            email = inputs['email']
            instagram_id = inputs['Instagram']
            if inputs.get('type') == None:
                raise Exception('type is empty')
            type = inputs['type']
            user = User.objects.create_user(username, email, password)
        except Exception as e:
            print(e)
        return redirect('accounts:signup')

    return render(request, 'signup.html', {'haserror' : False})