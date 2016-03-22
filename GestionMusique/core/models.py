from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Artist(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name.encode('utf8')

class Group(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name.encode('utf8')

class Genre(models.Model):
	label = models.CharField(max_length=200)
	def __str__(self):
		return self.label.encode('utf8')

class Song(models.Model):
	title = models.CharField(max_length=200)
	artist = models.ForeignKey(Artist)
	img = models.ImageField(null=True, upload_to='images')
	releaseYear = models.IntegerField()
	group = models.ForeignKey(Group)
	genres = models.ManyToManyField(Genre, through="Classification")
	def __str__(self):
		return self.title.encode('utf8')

class Classification(models.Model):
	song = models.ForeignKey(Song)
	genre = models.ForeignKey(Genre)
