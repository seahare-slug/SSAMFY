from django.urls import path
from . import views

urlpatterns = [
    path('movies/' ,views.movie_list, name='movie_list'),
    path('genres/',views.genre_list, name='genre_list')
]
