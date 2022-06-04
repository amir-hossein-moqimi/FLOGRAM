from django.shortcuts import render,redirect
from accounts.models import Profile, Request_Code
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import random
from . import mainbot
from django.utils import timezone
from django.shortcuts import get_object_or_404
import requests
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def create_code():
	characters = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
	return "".join(random.choices(characters, k=6))

def username_is_valid(username):
    allowed = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    for i in username:
        if i not in allowed:
            return False
    return True

def login(request):
    if request.method == 'POST':
        inputs = request.POST
        print(inputs)
        username = inputs['username']
        password = inputs['password']
        user = authenticate(request, username=username, password=password)
        if (user is not None) and (user.profile.verified):
            auth_login(request, user)
            if user.profile.type == 'Influencer':
                return redirect(settings.CURRENT_DOMAIN+"accounts/"+username)
            return redirect(settings.CURRENT_DOMAIN+"accounts/sponsors/")
        return render(request, 'login.html', {'haserror':True})
    return render(request, 'login.html', {'haserror':False})

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
            if not username_is_valid(username):
                raise Exception('Usernames can only contain letters and numbers')
            if password != inputs['Confirm']:
                raise Exception('password missmatch')
            if inputs.get('type') == None:
                raise Exception('type is empty')
            if not mainbot.id_exists(instagram_id):
                raise Exception("instagram id does not exist or your account is private")
            type = inputs['type']
            user = User.objects.create_user(username=username, password=password)
            user.profile.Instagram = instagram_id
            user.profile.email = email
            user.profile.type = type
            code = Request_Code(user=user)
            code.save()
            msg = f'Hey There! \nfirst add the following link to your bio on instagram:\n{settings.CURRENT_DOMAIN+"accounts/signup/"+username}\nThen please enter the following link to verify your account! \n {settings.CURRENT_DOMAIN +"accounts/verify/"+code.code}'
            try:
                send_mail('verification link!' ,
                    msg ,
                    settings.EMAIL_HOST_USER ,
                    [email])
            except:
                raise Exception("invalid email")
            user.save()
            user.profile.save()
            return redirect('homePage')
        except Exception as e:
            print('an error occured! : ',e)
            return render(request, 'signup.html', {'haserror' : True, 'error': e})

    return render(request, 'signup.html', {'haserror' : False})

def verify_code(request, code):
    code = get_object_or_404(Request_Code, code=code)
    verified_instagram = mainbot.verify_instagram(code.user.profile.Instagram, settings.CURRENT_DOMAIN+'accounts/signup/'+code.user.username)
    #code.user.profile.verified should not be true before verification but the admin can change it manaually to test
    if verified_instagram or code.user.profile.verified:
        code.user.profile.verified = True
        code.user.profile.save()
        if code.user.profile.type == 'Influencer':
            mainbot.download_profile(code.user.profile.Instagram)
        return render(request, 'verify.html', {'verified':True})
    else :
        return render(request, 'verify.html', {'verified':False})

@login_required(login_url='accounts:loginpage')
def sponsors(request):
    if request.user.profile.type == 'Influencer':
        return HttpResponse("<html><body>Influencers can not visit this page!</body></html>")
    else :
        influs = Profile.objects.filter(verified = True, type='Influencer')
        return render(request, 'sponsors.html', {'influs':influs})

@login_required(login_url='accounts:loginpage')
def influencers(request, username):
    if request.method == 'POST':
        inputs = request.POST
        user = request.user
        description = inputs['description']
        money = inputs['money']
        if money == '' or description == '':
            result = 'fill the forms!'
        else :
            user.profile.money = money
            user.profile.description = description
            user.profile.save()
            result = 'every thing submitted successfully!'
            return render(request, 'influencer.html', {'is_influencer':True, 'influencer':username, 'can_edit':True,'result':result,'id':user.profile.Instagram})
    else:
        requested = get_object_or_404(User, username=username)
        if requested.profile.type == 'Influencer':
            can_edit = False
            if requested == request.user :
                can_edit = True
            object = mainbot.Influencer(requested.profile.Instagram)
            return render(request, 'influencer.html', {'requested':requested, 'is_influencer':True, 'influencer':username, 'can_edit':can_edit,'result':None ,'id':requested.profile.Instagram, 'object':object})
        else:
            return redirect('accounts:sponsors')