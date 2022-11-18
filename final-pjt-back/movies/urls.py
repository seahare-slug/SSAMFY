from django.urls import path
from . import views

urlpatterns = [
    path('movies/' ,views.movie_list, name='movie_list'),
    path('genres/',views.genre_list, name='genre_list'),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/comment/create/', views.comment_create),
    path('movies/<int:movie_pk>/comment/', views.comment_view),
    path('movies/<int:comment_pk>/comment/delete/', views.comment_delete),
]
