from django.shortcuts import render

# Create your views here.


def settings(req):
    return render(req, 'users/settings.html')
