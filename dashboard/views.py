from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Corey',
        'title': 'Blog Post 1',
        'content': 'First Post',
        'date_posted': 'August 27, 2010'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 1',
        'content': 'Second Post',
        'date_posted': 'August 28, 2010'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'dashboard/home.html', context)


def logIn(request):
    return HttpResponse('<h1>This is login page! May be usefull in the future ;D</h1>')


def about(request):
    return render(request, 'dashboard/about.html', {'title': 'About Us'})
