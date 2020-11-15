from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='RateTheMovie-Dashboard'),
    path('login/', views.logIn, name='RateTheMovie-login'),
]