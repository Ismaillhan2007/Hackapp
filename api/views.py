import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_framework`')
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, permissions
from .forms import RegisterForm, LoginForm, EditProfileForm
from .models import CustomUser
from .serializers import UserSerializer
from django.conf import settings
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required


def is_superuser(user):
    return user.is_superuser 
# Web views
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            # # Check if user selected to be a superuser
            # if 'is_superuser' in request.POST:
            #     user.is_superuser = True
            #     user.is_staff = True
            user.save()
            login(request, user)
            return redirect('profile', username=user.username)
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    is_own_profile = request.user == user
    return render(request, 'users/profile.html', {'user': user, 'is_own_profile': is_own_profile})
# mistake possibly here
# API views
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    print("mistake is here")
    def get_queryset(self):
        if self.request.user.is_superuser:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id=self.request.user.id)#mistake could be here

# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Events.objects.all()
#     serializer_class = EventSerializer
# #mistake here
#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             return Events.objects.all()
#         if self.request.user.has_perm('api.manage_own_events'):
#             return Events.objects.filter(organizer=self.request.user)
#         return Events.objects.none()
    
#     def perform_create(self, serializer):
#         user = CustomUser.objects.get(id=self.request.user.id)
#         serializer.save(organizer=user)

