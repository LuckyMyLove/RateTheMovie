from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome in RateTheMovie!</h1>')


def logIn(request):
    return HttpResponse('<h1>This is login page! May be usefull in the future ;D</h1>')
