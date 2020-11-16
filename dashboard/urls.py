from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.logIn, name='login'),
    path('about/', views.about, name='about')
]
