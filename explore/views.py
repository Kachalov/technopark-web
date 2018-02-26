from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'explore/index.html', {
        'popular_tags': [
            'some', 'popular', 'tags', 'will', 'be', 'shown', 'here'],
        'best_members': ['Kachalov', 'Buglight', 'Anonymous'],
        'build': 'dev',
        'title': 'Explore',
        'login': 'Kachalov',
        'pages': 11,
        'page': 4,
        'questions': [
            dict(id=1, title='Question', desc='Desc', answers='42',
                 tags=['t1', 't2', 'really long #tag'],
                 author='Kachalov', rating=12),
            dict(id=1, title='Question 2', desc='Desc', answers='1',
                 tags=['tag'], author='Buglight', rating=7),
        ],
    })


def tag(request, tag):
    return render(request, 'explore/index.html', {
        'popular_tags': [
            'some', 'popular', 'tags', 'will', 'be', 'shown', 'here'],
        'best_members': ['Kachalov', 'Buglight', 'Anonymous'],
        'build': 'dev',
        'title': '#' + tag,
        'login': 'Kachalov',
        'pages': 11,
        'page': 4,
        'questions': [
            dict(id=1, title='Question 2', desc='Desc', answers='1',
                 tags=['tag'], author='Buglight', rating=7),
        ],
    })
