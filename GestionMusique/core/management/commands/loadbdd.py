from django.core.management.base import BaseCommand, CommandError
from core.models import *
import yaml

class Command(BaseCommand):
	help = "Load the database"

	def add_arguments(self,parser):
		parser.add_argument('filename',nargs='1',type=str)

	def handle(self,**option):
		songs = yaml.load(open(option['filename'][0]))

		for s in songs:
			a,isNew = Author.objects.get_or_create( name=s['by'])
			if isNew:
				a.save()

			si,isNew = Singer.objects.get_or_create( name=s['parent'])
			if isNew:
				si.save()
			song,isNew = Song.objects.get_or_create( id=s['enterId'], title=s['title'], author=a, img=s['img'], releaseYear=s['releaseYear'], singer=si)
			for genre in s['genre']:
				g,isNew = Genre.objects.get_or_create( label=genre)
				c,_ =Classification.objects.get_or_create(song=song,genre=g)
				if isNew:
					g.save()

		self.stdout.write("Database loaded")