from django.shortcuts import render

# Create your views here.


def questions(req, p=1):
    return render(req, 'questions/index.html', {
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


def question(req, q):
    return render(req, 'questions/question.html')
