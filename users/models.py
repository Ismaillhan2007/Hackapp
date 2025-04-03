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
    
    # # Add related_name to resolve the naming conflicts
    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='custom_user_set',
    #     blank=True,
    #     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    #     verbose_name='groups',
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='custom_user_set',
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     verbose_name='user permissions',
    # )

    def __str__(self):
        return self.username
