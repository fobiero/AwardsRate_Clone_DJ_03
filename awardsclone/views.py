
from django.shortcuts import render, HttpResponse

posts = [
    {
        'author' : 'Paul Walker', 
        'title' : 'Making it look right ', 
        'content' : 'Lorem ipsum finds people unawre',
        'date_posted' : 'August 20th, 2000'
    }, 
    {
        'author' : 'jane Doe', 
        'title' : 'Second Post',
        'content' : 'I wish things would be better',
        'date_posted' : 'May 16th, 2030'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render (request, 'index.html', context)