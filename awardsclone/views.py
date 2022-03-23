
from django.shortcuts import render,redirect, HttpResponse
from .models import *

posts = [
    {
        'title' : 'Project title', 
        'location' : 'Netherlands ', 
        'date_posted' : 'August 20, 2000',
        'author' : 'author name',
    }, 
    {
        'title' : 'Project title', 
        'location' : 'Sweden', 
        'date_posted' : 'August 14, 1980',
        'author' : 'author name',
    },
    {
        'title' : 'Project title', 
        'location' : 'Germany', 
        'date_posted' : 'September 14, 2004',
        'author' : 'author name',
    }
]

def home(request):
    return HttpResponse(request, 'gettin started')


# def home(request):
#     data = {
#         'posts' : posts
#     }

#     return render(request, 'index.html', data)

