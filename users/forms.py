from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password')

class EditForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea,required=False,label="About myself")
    avatar = forms.ImageField(required=False,label="Avatar")
    email = forms.EmailField(required=True,label="Email")
    
    class Meta:
        model = CustomUser
        fields = ('bio','avatar','email')

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True,label="Username")
    password = forms.CharField(required=True,widget=forms.PasswordInput,label="Password")
    
    class Meta:
        model = CustomUser
        fields = ('username','password')
        