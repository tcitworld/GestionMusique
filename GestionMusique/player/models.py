from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Artist(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Group(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Genre(models.Model):
	label = models.CharField(max_length=200)
	def __str__(self):
		return self.label

class Album(models.Model):
	title = models.CharField(max_length=200)
	artist = models.ForeignKey(Artist)
	img = models.ImageField(null=True, upload_to='images')
	releaseYear = models.IntegerField()
	group = models.ForeignKey(Group)
	genres = models.ManyToManyField(Genre, through="Classification")
	def __str__(self):
		return self.title

class Classification(models.Model):
	album = models.ForeignKey(Album)
	genre = models.ForeignKey(Genre)

class Song(models.Model):
	album = models.ForeignKey(Album)

class PlayList(models.Model):
	songs = models.ManyToManyField(Song,through="Selection")

class Selection(models.Model):
	song = models.ForeignKey(Song)
	playlist = models.ForeignKey(PlayList)