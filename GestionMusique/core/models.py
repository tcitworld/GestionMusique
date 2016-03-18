from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=200,null=True)

class Singer(models.Model):
	name = models.CharField(max_length=200)

class Genre(models.Model):
	label = models.CharField(max_length=200)
	def __str__(self):
		return self.label

class Song(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(Author)
	img = models.CharField(max_length=200,null=True)
	releaseYear = models.IntegerField()
	singer = models.ForeignKey(Singer)
	genres = models.ManyToManyField(Genre, through="Classification")

class Classification(models.Model):
	song = models.ForeignKey(Song)
	genre = models.ForeignKey(Genre)
