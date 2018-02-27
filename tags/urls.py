from django.urls import path

from . import views

urlpatterns = [
    path('tag/<tag>/', views.tag, name='tag'),
]
