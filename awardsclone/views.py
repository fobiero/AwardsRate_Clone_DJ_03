
from django.shortcuts import render, HttpResponse

posts = [
    {
        'title' : 'Project titlle', 
        'location' : 'Netherlands ', 
        'date_posted' : 'August 20, 2000',
        'author' : 'author name',
    }, 
    {
        'title' : 'Project tile', 
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
    data = {
        'posts' : posts
    }

    return render (request, 'index.html', data)