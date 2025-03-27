from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, EditForm
from .models import CustomUser

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser

def home(request):
    return render(request, 'base.html')


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            is_superuser = request.POST.get('is_superuser',False)
            if is_superuser:
                user.is_superuser = True
            user.save()
            login(request,user)
            return redirect('users:profile', username=user.username)
    else:
        form = RegisterForm()
    return render (request,'register.html',{'form':form})
            