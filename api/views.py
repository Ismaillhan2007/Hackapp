from django.shortcuts import render

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, permissions
from .forms import RegisterForm, LoginForm, EditProfileForm
from .models import CustomUser, Events
from .serializers import UserSerializer, EventSerializer
from django.conf import settings
# Web views
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            # Check if user selected to be a superuser
            if 'is_superuser' in request.POST:
                user.is_superuser = True
                user.is_staff = True
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

# API views
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id=self.request.user.id)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Events.objects.all()
        if self.request.user.has_perm('api.manage_own_events'):
            return Events.objects.filter(organizer=self.request.user)
        return Events.objects.none()
    
    def perform_create(self, serializer):
        user = CustomUser.objects.get(id=self.request.user.id)
        serializer.save(organizer=user)