from .models import Movie,Genre, Comment
from .serializer import MovieSerializer,GenreSerializer, CommentSerializer, CommnetListSerializer
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
    movie = Movie.objects.get(pk=movie_pk)
    comment_serializer = CommentSerializer(data=request.data)
    if comment_serializer.is_valid():
        comment_serializer.save(movie=movie)
        return Response(comment_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def comment_view(request, movie_pk):
    comments = Comment.objects.filter(movie_id=movie_pk)
    serializer = CommnetListSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def comment_delete(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)