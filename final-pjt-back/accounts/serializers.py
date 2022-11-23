from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username",)

class LikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "liked_movie",)
    