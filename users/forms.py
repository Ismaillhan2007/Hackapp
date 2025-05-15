from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .models import Events


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password','avatar')

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

class LogoutForm(forms.Form):
    confirm_logout = forms.BooleanField(
        required=True,
        label="Confirm Logout",
        help_text="Check this box to confirm you want to logout"
    )
        

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('title','description','date','location')
        

