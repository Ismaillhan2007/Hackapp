from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.home, name='home'),
    path('events/create/', views.create_event, name='create_event'),
   path('events/<int:event_id>/', views.home, name='event_detail'),  # Redirects to home
    path('events/<int:event_id>/edit/', views.home, name='edit_event'),  # Redirects to home
    path('events/<int:event_id>/register/', views.home, name='register_for_event'),  # Redirects to home
    path('register/', views.register_user, name='register'),
    path('login/',views.login_view, name = 'login'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('logout/',views.logout_view,name = 'logout'),
]

