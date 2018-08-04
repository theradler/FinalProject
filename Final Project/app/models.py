"""
Definition of models.
"""

from django.db import models
import uuid

# Create your models here
class Movies(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=50, editable=True, blank=False)
    details = models.CharField(max_length=100)