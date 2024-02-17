from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
<<<<<<< HEAD

=======
>>>>>>> 7ee1b9e702d63fb56b707c867c05c5b33ede353f
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
<<<<<<< HEAD
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form = LoginForm), name='login')
=======
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html' , authentication_form= LoginForm), name='login'),
    
>>>>>>> 7ee1b9e702d63fb56b707c867c05c5b33ede353f
]
