from django.urls import path

from . import views

urlpatterns = [
    path('<tag>', views.tag, name='tag'),
]