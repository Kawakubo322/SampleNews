from django.db import models
from django.conf import settings

from newsapi import NewsApiClient

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()