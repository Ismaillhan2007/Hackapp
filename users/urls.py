from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'users'

urlpatterns = [
    path('',views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    
]
