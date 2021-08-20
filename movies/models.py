from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_organisor = models.BooleanField(default=False)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=3000, default=" ")
    date_released = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    reviews = models.IntegerField(default=0)
    poster = models.ImageField(default="default.jpeg", upload_to='movie_posters')

    def __str__(self):
	    return self.title

class Review(models.Model):
    title = models.ForeignKey(Movie, on_delete=CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    details = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) 

    def __str__(self):
    	return self.details

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(default='')
    date_posted = models.DateTimeField(default=timezone.now) 

    def __str__(self):
	    return self.comment