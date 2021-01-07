from django.urls import path
from .views import moviesDetails, actorsDetails, directorsDetails
from . import views

urlpatterns = [
    path('', views.movies, name='movies'),
    path('movies/', views.movies, name='movies'),
    path('movies/<int:pk>/', moviesDetails.as_view(), name='moviesDetails'),
    path('about/', views.about, name='about'),
    path('actors/', views.actors, name='actors'),
    path('actors/<int:pk>/', actorsDetails.as_view(), name='actorsDetails'),
    path('directors/', views.directors, name='directors'),
    path('directors/<int:pk>/', directorsDetails.as_view(), name='directorsDetails'),
]
