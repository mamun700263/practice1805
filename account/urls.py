"""
URL configuration for practice1805 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import  *
urlpatterns = [
path('',home,name='Home'),
path('registration/',registration,name='Registration'),
path('profile/',profile,name='profile'),
path('login/',user_login,name='login'),
path('logout/',user_logout,name='logout'),
path('change_pass/',change_pass_with_old,name='change_pass_with_old'),
path('change_pass_old/',change_pass_without_old,name='change_pass_without_old'),
path('change_user_info/',change_user_info,name='change_user_info'),
]
