from django.urls import path

from questions.views import questions as explore_view

urlpatterns = [
    path('', explore_view, name='explore'),
]
