from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Singer(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Genre(models.Model):
	label = models.CharField(max_length=200)
	def __str__(self):
		return self.label

class Song(models.Model):
	id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=200)
	author = models.OneToOneField(Author)
	img = models.CharField(max_length=200)
	releaseYear = models.IntegerField()
	singer = models.OneToOneField(Singer)
	genres = models.ManyToManyField(Genre, through="Classification")

class Classification(models.Model):
	song = models.ForeignKey(Song)
	genre = models.ForeignKey(Genre)
