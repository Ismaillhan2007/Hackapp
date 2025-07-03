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


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='users_customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='users_customuser_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username









