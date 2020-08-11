import os

from django.conf import settings
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import *


# Create your views here.


def login(request):
    login_form = LoginForm(data=request.POST)
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password1)
            if user is not None and user.is_active:
                auth.login(request, user)
                user_dir = settings.MEDIA_ROOT + '\\homework\\' + str(user.uuid) + '\\'
                if not os.path.exists(user_dir):
                    os.mkdir(user_dir)
                return HttpResponseRedirect(reverse('main:index'))
    content = {'login_form': login_form}
    return render(request, 'authapp/form-login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            HttpResponseRedirect(reverse('main:index'))
    else:
        register_form = RegisterForm()
    content = {'register_form': register_form}
    return render(request, 'authapp/form-register.html', content)


@login_required
def profile(request):
    return render(request, 'authapp/user-profile.html')