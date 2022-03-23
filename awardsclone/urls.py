
from django.urls import path  
from django.contrib import admin  
from . import views  

urlpatterns = [
    path('', views.home, name='homePage'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
