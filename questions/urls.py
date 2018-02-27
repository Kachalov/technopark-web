from django.urls import path

from . import views

urlpatterns = [
    path('<int:q>', views.question, name='question'),
    path('p<int:p>', views.questions, name='questions'),
    path('new', views.new_question, name='new_question'),
]
