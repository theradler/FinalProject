"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here
class Movies(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=50, editable=True, blank=False)
    details = models.CharField(max_length=100)

class UserMovieList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movies', on_delete=models.SET_NULL, null=True)
    list_postition = models.IntegerField()
