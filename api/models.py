from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from rest_framework import serializers
from django.contrib.auth import get_user_model 

class CustomUser(AbstractUser):
    bio = models.TextField(max_length = 500,blank=True,default='Edit me please',verbose_name="About myself")
    city = models.CharField(max_length=100,blank=True)
    avatar = models.ImageField(upload_to='avatars/',blank=True,null=True,verbose_name='avatar')
    email = models.EmailField(max_length=25,blank=True)  

    def __str__(self):
        return self.username
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='api_customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='api_customuser_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Events(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    date =  models.DateTimeField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 
