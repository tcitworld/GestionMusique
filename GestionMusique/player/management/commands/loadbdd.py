# coding: utf8

from django.core.management.base import BaseCommand, CommandError
from player.models import *
import yaml,sys,urllib.parse

class Command(BaseCommand):
	help = "Load the database"

	def add_arguments(self,parser):
		parser.add_argument('filename',nargs='+',type=str)

	def handle(self,**option):
		albums = yaml.load(open(option['filename'][0]))
		tt = 100
		for i in range(1,tt):
			s = albums[i]
			if s['by'] != 'X' or s['by'] != None or s['by'] != 'null':
				a,isNew = Artist.objects.update_or_create( name=s['by'])
			else:
				a,isNew = Artist.objects.update_or_create( name="inconnue")
			if isNew:
				a.save()
			if s['parent'] != 'null' or s['parent'] != None:
				si,isNew = Group.objects.update_or_create( name=s['parent'])
			else:
				si,isNew = Group.objects.update_or_create( name="inconnue")
			if isNew:
				si.save()
			album,isNew = Album.objects.update_or_create(title=s['title'], artist=a, img=urllib.parse.quote(s['img']) if s['img'] != None else None, releaseYear=s['releaseYear'], group=si)
			if isNew:
				album.save()
			for genre in s['genre']:
				g,isNew = Genre.objects.update_or_create( label=genre)
				if isNew:
					g.save()
				c,isNew = Classification.objects.update_or_create(album=album,genre=g)
				if isNew:
					c.save()

			sys.stdout.write("Chanson n° "+ str(i).ljust(6," ") + " | " + str(int(i/(tt-1)*100)).rjust(4," ") + " % en cours" + chr(13))
			sys.stdout.flush()

		self.stdout.write("Database loaded")
