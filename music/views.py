from django.shortcuts import render, redirect
from .models import Song
from .models import Album
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from . import forms
from django.http import HttpResponse
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

@login_required
def edit_songs(request):
	songs = Song.objects.all()
	return render(request, 'music/edit_songs.html', {'songs': songs})


@login_required
def manage_songs(request):
	if request.method == 'POST':
		form = forms.CreateSong(request.POST, request.FILES)
		if form.is_valid():
			# save article todb
			instance = form.save(commit=False)
			return redirect('dashboard:index')
	else:
		form = forms.CreateSong()	
	return render(request, "music/manage_songs.html", {'form': form})

class SongUpdate(UpdateView):
	model = Song
	form_class = forms.SongForm
	template_name_suffix = '_update_form'
	context_object_name = 'song'

	def form_valid(self, form):
		song = form.save(commit=False)
		song.save()
		return redirect("music:media")