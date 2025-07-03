from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    register_user,
    profile, 
    UserViewSet,
)

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
app_name = 'api'

urlpatterns = [
    # Web URLs
    path('register/', views.register_user, name='register'),
    path('profile/<str:username>/', views.profile, name='profile'),
    # API URLs
    path('', include(router.urls)),
    path('', include(router.urls)),
]