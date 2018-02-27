from django.urls import path

from . import views

urlpatterns = [
    path('settings/', views.settings, name='settings'),
    path('login/', views.login, name='login'),
    path('signup/', views.register, name='signup'),
]
