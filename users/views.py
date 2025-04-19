from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, EditForm, LogoutForm
from .models import CustomUser
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .models import Events,EventsRegistration
from .forms import EventForm
from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    events = Events.objects.all().order_by('-date')
    return render(request, 'home.html',{'events':events})


def is_superuser(user):
    return user.is_superuser 


@login_required
@user_passes_test(is_superuser) 
def create_event(request):
    print("Here is mistake")
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('users:event_detail',event_id = event.id)
    else:
        form = EventForm()
    return render(request,'create_event.html', {'form':form })

def event_detail(request,event_id):
    event = get_object_or_404(Events, id = event_id)
    is_registered = request.user.is_authenticated and EventsRegistration.objects.filter(event=event, user=request.user).exists()
    return render(request,'home.html',{
        'event': event,
        'is_registered': is_registered,
    })

@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Events, id = event_id)
    if request.method == 'POST':
        # Check if already registered
        if not EventsRegistration.objects.filter(event=event, user=request.user).exists():
            EventsRegistration.objects.create(event=event, user=request.user)
        return redirect('users:event_detail', event_id=event.id)
    return render(request, 'home.html', {'event': event})

# Edit event (superusers only)
@user_passes_test(is_superuser)
def edit_event(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('users:event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'home.html', {'form': form})


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




    
   
