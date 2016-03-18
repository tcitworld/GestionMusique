from django.core.management.base import BaseCommand, CommandError
from core.models import *
import yaml,sys

class Command(BaseCommand):
	help = "Load the database"

	def add_arguments(self,parser):
		parser.add_argument('filename',nargs='+',type=str)

	def handle(self,**option):
		songs = yaml.load(open(option['filename'][0]))
		i = 0;
		tt = len(songs)
		for i in range(1,tt):
			s = songs[i]
			a,isNew = Author.objects.get_or_create( name=s['by'])
			if isNew:
				a.save()
			si,isNew = Singer.objects.get_or_create( name=s['parent'])
			if isNew:
				si.save()
			song,isNew = Song.objects.get_or_create(title=s['title'], author=a, img=s['img'], releaseYear=s['releaseYear'], singer=si)
			if isNew:
				song.save()
			for genre in s['genre']:
				g,isNew = Genre.objects.get_or_create( label=genre)
				if isNew:
					g.save()
				c,isNew = Classification.objects.get_or_create(song=song,genre=g)
				if isNew:
					c.save()

			sys.stdout.write("Chanson n° "+ str(i).ljust(6," ") + " | " + str(int(i/tt*100)).ljust(4," ") + " % en cours" + chr(13))
			sys.stdout.flush()

		self.stdout.write("Database loaded")
