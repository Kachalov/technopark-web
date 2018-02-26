from django.shortcuts import render

# Create your views here.


def tag(request, tag):
    return render(request, 'questions/index.html', {
        'title': '#' + tag,
        'login': 'Kachalov',
        'pages': 11,
        'page': 4,
        'questions': [
            dict(id=1, title='Question 2', desc='Desc', answers='1',
                 tags=['tag'], author='Buglight', rating=7),
        ],
    })
