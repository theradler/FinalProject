"""
Definition of models.
"""

from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
import uuid


# Create your models here
class Movies(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    moviedb_id = models.CharField(max_length=5,unique=True, null=True,default=None )
    title = models.CharField(max_length=50, editable=True, blank=False)
    poster_path = models.CharField(max_length=50, editable=False, blank=True, null=True)
    details = models.CharField(max_length=1000)

class UserMovieList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movies', on_delete=models.SET_NULL, null=True)
    list_position = models.IntegerField()

class Comments(models.Model):
    userList = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    commentOwner = models.CharField(max_length=120,null=True)
    comments = models.CharField(max_length=120)

class MovieReviews(models.Model):
    movie = models.ForeignKey('Movies', on_delete=models.CASCADE, null=True)
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True)
    movie_rating = models.IntegerField()
    movie_review_text = models.CharField(max_length=1000)