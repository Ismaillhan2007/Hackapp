from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    register_user,
    profile, 
    UserViewSet,
    EventViewSet,
)

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'events', views.EventViewSet)

app_name = 'api'

urlpatterns = [
    # Web URLs
    path('register/', views.register_user, name='register'),
    path('profile/<str:username>/', views.profile, name='profile'),
    # API URLs
    path('', include(router.urls)),
    path('', include(router.urls)),
]