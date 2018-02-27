from django.urls import path

from . import views

urlpatterns = [
    path('tag/<tag>/', views.tag, name='tag'),
    path('tag/<tag>/<int:p>', views.tag, name='tag'),
]
