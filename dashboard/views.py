from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Avg
from .models import *
from .forms import *



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


def about(request):
    return render(request, 'dashboard/about.html', {'title': 'About Us'})


def movies(request):
    movies = Movies.objects.all()
    movieRatings = Movies_rates.objects.all().values('movie_id').annotate(avg_rate=Avg('rate'))
    moviesDirectors = Movies_directors.objects.all()
    moviesActors = Movies_Actors.objects.all()
    categories = Categories.objects.all()
    form = MoviesForm()

    context = {
        'moviesData': movies,
        'movieRatings': movieRatings,
        'moviesDirectors': moviesDirectors,
        'moviesActors': moviesActors,
        'categories': categories,
        'form': form
    }
    if request.method == 'POST':
        form = MoviesForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/movies/')

    return render(request, 'dashboard/movies.html', context)


def actors(request):
    obj = Actors.objects.all()
    actorsRatings = ActorsRates.objects.all().values('actors_id').annotate(avg_rate=Avg('rate'))
    form = ActorsForm()
    context = {
        'data': obj,
        'ratings': actorsRatings,
        'form': form
    }

    if request.method == 'POST':
        form = ActorsForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/actors/')

    return render(request, 'dashboard/actors_directors.html', context)



def directors(request):
    obj = Directors.objects.all()
    directorsRatings = DirectorsRates.objects.all().values('director_id').annotate(avg_rate=Avg('rate'))
    form = DirectorsForm()
    context = {
        'data': obj,
        'ratings': directorsRatings,
        'form': form
    }
    if request.method == 'POST':
        form = DirectorsForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/directors/')

    return render(request, 'dashboard/actors_directors.html', context)


