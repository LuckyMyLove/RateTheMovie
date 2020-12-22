from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Avg
from django.db import transaction
from django.views.generic import DetailView
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
    movie_ratings = MoviesRates.objects.all().values('movie_id').annotate(avg_rate=Avg('rate'))
    moviesDirectors = MoviesDirectors.objects.all()
    moviesActors = MoviesActors.objects.all()
    categories = Categories.objects.all()
    form = MoviesForm()
    category_form = CategoryForm()

    context = {
        'moviesData': movies,
        'movieRatings': movie_ratings,
        'moviesDirectors': moviesDirectors,
        'moviesActors': moviesActors,
        'categories': categories,
        'form': form,
        'categoryForm': category_form
    }
    if request.method == 'POST':
        if 'categories' in request.POST:
            context['moviesData'] = Movies.objects.filter(category_id=request.POST['categories'])
        else:
            form = MoviesForm(request.POST)
            if form.is_valid():
                with transaction.atomic():
                    movie = form.save()
                    actor_id = int(form.data.get('actors'))
                    director_id = form.data.get('directors')
                    updateMoviesActors(actor_id, movie.id)
                    updateMovieDirectors(director_id, movie.id)
            return HttpResponseRedirect('/movies/')

    return render(request, 'dashboard/movies.html', context)


def updateMoviesActors(actor_id, movie_id):
    movie_actors = MoviesActors()
    movie_actors.movie_id = movie_id
    movie_actors.actor_id = actor_id
    movie_actors.save()


def updateMovieDirectors(director_id, movie_id):
    movie_director = MoviesDirectors()
    movie_director.movie_id= movie_id
    movie_director.director_id = director_id
    movie_director.save()


class moviesDetails(DetailView):
    model = Movies
    template_name = 'dashboard/movies_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rates'] = MoviesRates.objects.all().values('movie_id').annotate(avg_rate=Avg('rate'))
        context['specificRates'] = MoviesRates.objects.all()
        context['moviesActors'] = MoviesActors.objects.all()
        context['moviesDirectors'] = MoviesDirectors.objects.all()

        return context


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


class actorsDetails(DetailView):
    model = Actors
    template_name = 'dashboard/actors_directors_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rates'] = ActorsRates.objects.all().values('actors_id').annotate(avg_rate=Avg('rate'))
        context['specificRates'] = ActorsRates.objects.all()
        context['moviesConnection'] = MoviesActors.objects.all()

        return context


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


class directorsDetails(DetailView):
    model = Directors
    template_name = 'dashboard/actors_directors_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rates'] = DirectorsRates.objects.all().values('director_id').annotate(avg_rate=Avg('rate'))
        context['specificRates'] = DirectorsRates.objects.all()
        context['moviesConnection'] = MoviesDirectors.objects.all()

        return context
