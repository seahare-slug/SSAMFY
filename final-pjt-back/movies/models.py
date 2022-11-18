from django.db import models

# Create your models here.
class Genre(models.Model):
	name = models.CharField(max_length=30)


class Movie(models.Model):
	adult = models.BooleanField()
	backdrop_path = models.CharField(max_length=100)
	genre_ids = models.ManyToManyField(Genre, related_name='movie_genres')
	original_language = models.TextField()
	original_title = models.TextField()
	overview = models.TextField()
	popularity = models.FloatField()
	poster_path = models.CharField(max_length=100)
	release_date = models.DateField()
	title = models.CharField(max_length=100)
	video = models.BooleanField()
	vote_average = models.FloatField()
	vote_count = models.IntegerField()

class Comment(models.Model):
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	content = models.TextField()
	username = models.CharField(max_length=100)