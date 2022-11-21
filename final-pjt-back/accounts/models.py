from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Comment

# Create your models here.


class User(AbstractUser):
    liked_movie = models.ManyToManyField(Movie, related_name="r_liked_movie")
    user_comment = models.ManyToManyField(Comment, related_name="r_user_comment")
