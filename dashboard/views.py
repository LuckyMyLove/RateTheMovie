from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Avg
from .models import *

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

def movies(request):
    movies = Movies.objects.all()
    movieRatings = Movies_rates.objects.all().values('movie_id').annotate(avg_rate=Avg('rate'))
    moviesDirectors = Movies_directors.objects.all()
    moviesActors = Movies_Actors.objects.all()

    context = {
        'moviesData': movies,
        'movieRatings': movieRatings,
        'moviesDirectors': moviesDirectors,
        'moviesActors': moviesActors
    }
    return render(request, 'dashboard/movies.html', context)

def about(request):
    return render(request, 'dashboard/about.html', {'title': 'About Us'})

def actors(request):
    obj = Actors.objects.all()
    context = {
        'data': obj,
    }
    return render(request, 'dashboard/actors_directors.html', context)

def directors(request):
    obj = Directors.objects.all()
    context = {
        'data': obj,
    }
    return render(request, 'dashboard/actors_directors.html', context)
