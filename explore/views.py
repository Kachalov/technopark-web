from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'explore/index.html', {
        'build': 'dev',
        'title': 'Explore',
        'login': 'Kachalov',
    })