from django.shortcuts import render
from .models import Movie,Genre
from .serializer import MovieSerializer,GenreSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def genre_list(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, movie_pk):
    print("URL은 통과 >>>>>>>>>>>>>>>>>>>")
    movie = Movie.objects.get(pk=movie_pk)
    comment_serializer = CommentSerializer(data=request.data)
    print("serializer은 통과 >>>>>>>>>>>>>>>>>>>")
    if comment_serializer.is_valid(raise_exception=True):
        print("IF 통과 >>>>>>>>>>>>>>>>>>>")
        comment_serializer.save(movie=movie)
        print("=====성공적으로 저장=====")
        return Response(comment_serializer.data, status=status.HTTP_201_CREATED)