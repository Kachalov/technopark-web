from django.urls import path

from . import views

urlpatterns = [
    path('settings', views.settings, name='settings'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
