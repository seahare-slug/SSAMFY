from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username",)

class LikedSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    liked_movie_id = serializers.IntegerField()
    