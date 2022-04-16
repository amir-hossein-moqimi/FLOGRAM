from django.shortcuts import render,redirect
from accounts.models import Profile
from django.contrib.auth.models import User

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        inputs = request.POST
        print(inputs)
        try:
            username = inputs['username']
            password = inputs['password']
            email = inputs['email']
            instagram_id = inputs['Instagram']
            if username == '' or password == '' or email == '' or instagram_id == '':
                raise Exception('some fields are empty')
            if password != inputs['Confirm']:
                raise Exception('password missmatch')
            if inputs.get('type') == None:
                raise Exception('type is empty')
            type = inputs['type']
            user = User.objects.create_user(username=username, password=password)
            user.profile.Instagram = instagram_id
            user.profile.email = email
            user.profile.type = type
            user.save()
            user.profile.save()
            return redirect('accounts:loginpage')
        except Exception as e:
            return render(request, 'signup.html', {'haserror' : False, 'error': e})

    return render(request, 'signup.html', {'haserror' : False})