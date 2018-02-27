from django.urls import path

from . import views

urlpatterns = [
    path('question/<int:q>', views.question, name='question'),
    path('hot/', views.questions, name='hot'),
    path('hot/<int:p>', views.questions, name='hot'),
    path('questions/', views.questions, name='questions'),
    path('questions/<int:p>', views.questions, name='questions'),
    path('ask/', views.new_question, name='new_question'),
]
