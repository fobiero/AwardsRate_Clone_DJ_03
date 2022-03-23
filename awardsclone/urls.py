
from django.urls import path  
from django.contrib import admin  
from . import views  
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='homePage'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login')
]
