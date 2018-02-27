from django.shortcuts import render

# Create your views here.


def settings(req):
    return render(req, 'users/settings.html')


def register(req):
    return render(req, 'users/register.html')


def login(req):
    return render(req, 'users/login.html')
