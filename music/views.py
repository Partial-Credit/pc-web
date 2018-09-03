from django.shortcuts import render
from .models import Song
from .models import Album
# Create your views here.
import sys
sys.path.append(sys.path[0] + "\\users")
from users.models import Member

def addMoreSongs():
	for i in range(15):
		obj = Song.objects.get(pk = 2)
		print(obj)	

def media(request):
	songs = Song.objects.all()
	albums = Album.objects.all()
	return render(request, 'music/media.html', {'songs': songs, 'albums': albums})