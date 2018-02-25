from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tags/<tag>', views.tag, name='tag'),
]
