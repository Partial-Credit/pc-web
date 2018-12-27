from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Song
from .models import Album
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
def edit_albums(request):
	albums = Album.objects.all()
	return render(request, 'music/edit_albums.html', {'albums': albums})

class SongCreate(CreateView):
	model = Song
	form_class = forms.SongForm
	template_name = "music/manage_songs.html"
	success_url = reverse_lazy('dashboard:index')

	def get_context_data(self, **kwargs):
		context = super(SongCreate, self).get_context_data(**kwargs)
		context['method']= 'Create'
		return context

class SongUpdate(UpdateView):
	model = Song
	form_class = forms.SongForm
	template_name = "music/manage_songs.html"
	context_object_name = 'song'
	success_url = reverse_lazy('music:edit_songs')		
	
	def get_context_data(self, **kwargs):
		context = super(SongUpdate, self).get_context_data(**kwargs)
		context['method']= 'Update'
		return context

class SongDelete(DeleteView):
	model = Song
	template_name = "music/confirm_delete.html"
	success_url = reverse_lazy('music:edit_songs')



class AlbumCreate(CreateView):
	model = Album
	form_class = forms.AlbumForm
	template_name = "music/manage_albums.html"
	success_url = reverse_lazy('dashboard:index')

	def get_context_data(self, **kwargs):
		context = super(AlbumCreate, self).get_context_data(**kwargs)
		context['method']= 'Create'
		return context

class AlbumUpdate(UpdateView):
	model = Album
	form_class = forms.AlbumForm
	context_object_name = 'album'
	template_name = "music/manage_albums.html"
	context_object_name = 'album'
	success_url = reverse_lazy('music:edit_albums')	

	def get_context_data(self, **kwargs):
		context = super(AlbumUpdate, self).get_context_data(**kwargs)
		context['method']= 'Update'
		return context

class AlbumDelete(DeleteView):
	model = Album
	template_name = "music/confirm_delete.html"
	success_url = reverse_lazy('music:edit_albums')




