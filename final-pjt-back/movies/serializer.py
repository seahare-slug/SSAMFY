from rest_framework import serializers
from .models import Movie,Genre, Comment

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("content", "username", "created_at",)

class CommnetListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"