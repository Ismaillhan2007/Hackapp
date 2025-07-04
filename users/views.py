from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, EditForm, LogoutForm
from .models import CustomUser
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
 

def home(request):
    if request.user.is_authenticated:
        return redirect('users:profile', username=request.user.username)
    return render(request, 'home.html')
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request,user)
            return redirect('users:profile', username=user.username)
    else:
        form = RegisterForm()
    return render (request,'register.html',{'form':form})
            

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:profile', username=user.username)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, 'profile.html', {'profile_user': user})


@login_required
def edit_profile(request):
    user = request.user 
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:profile', username=user.username)
        else:
            return render(request, 'edit_profile.html', {'form': form})
    return render(request, 'edit_profile.html', {'form': EditForm(instance=user)})

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:home')


   
