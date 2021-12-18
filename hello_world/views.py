from django.shortcuts import render
from hello_world.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from hello_world.models import UserProfileInfo
 
# Create your views here.
def index(request):
    return render(request,'hello_world/index.html')
 
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
 
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False) #commit=False store in memory first instead of store in database 
            # memory storing (occupation... ) temporarily save is because we need to capture user id
            profile.user=user # capture user id
            profile.save() # save profile
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else: # if GET request
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
 
    return render(request,'hello_world/registration.html',
    {'user_form':user_form,
    'profile_form':profile_form,
    'registered':registered}
    )
 
def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request,'hello_world/login.html')