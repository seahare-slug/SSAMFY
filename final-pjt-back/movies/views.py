from django.shortcuts import render
from .models import Movie,Genre
from .serializer import MovieSerializer,GenreSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        # articles = get_list_or_404(Article)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def genre_list(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        # articles = get_list_or_404(Article)
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    
