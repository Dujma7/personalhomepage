from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    imageUrl = models.CharField(max_length=2040)

    def __str__(self):
        return str(self.title) + " | " + str(self.author)


class Project(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    urlToSite = models.CharField(max_length=2040)
    imageUrl = models.CharField(max_length=2040)

    def __str__(self):
        return str(self.title) + " | " + str(self.author)


class ChessGame(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    pgn = models.TextField()

    def __str__(self):
        return "Game " + str(self.id)
