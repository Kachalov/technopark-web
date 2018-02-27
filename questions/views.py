from django.shortcuts import render

# Create your views here.


def questions(req, p=1):
    return render(req, 'questions/index.html', {
        'title': 'Explore',
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


def hot(req, p=1):
    return questions(req, p)


def question(req, q):
    return render(req, 'questions/question.html', {
        'title': 'Question ' + str(q),
        'q': dict(id=1, title='Question ' + str(q), desc='Desc', answers='42',
                  tags=['t1', 't2', 'really long #tag'],
                  author='Kachalov', rating=12),
        'comments': [
            dict(id=x, desc='Desc ' + str(x), author='Kachalov', rating=12)
            for x in range(1, 10)
        ],
    })


def new_question(req):
    return render(req, 'questions/new.html', {
        'title': 'New question',
    })
