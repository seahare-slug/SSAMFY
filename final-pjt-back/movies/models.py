from django.db import models

# Create your models here.

class Movie(models.Model):
	adult = models.BooleanField()
	backdrop_path = models.CharField(max_length=100)
	id = models.IntegerField(primary_key=True)
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