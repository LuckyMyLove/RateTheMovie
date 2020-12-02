from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies, name='movies'),
    path('movies/', views.movies, name='movies'),
    path('about/', views.about, name='about'),
    path('actors/', views.actors, name='actors'),
    path('directors/', views.directors, name='directors'),

    path('home/', views.home, name='home')
]
