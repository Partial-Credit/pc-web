from django.shortcuts import render
from .models import Song
# Create your views here.
import sys
sys.path.append(sys.path[0] + "\\users")
from users.models import Member

def addMoreSongs():
	for i in range(15):
		obj = Song.objects.get(pk = 2)
		print(obj)
		# obj.pk = None
		# obj.save()	

def media(request):
	songs = Song.objects.all()
	print(songs)
	test= list()
	return render(request, 'music/media.html', {'songs': songs})