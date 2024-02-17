from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
<<<<<<< HEAD

=======
>>>>>>> 7ee1b9e702d63fb56b707c867c05c5b33ede353f
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
<<<<<<< HEAD
        'placeholder': 'Enter your username',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your Password',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    
=======
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

>>>>>>> 7ee1b9e702d63fb56b707c867c05c5b33ede353f
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))