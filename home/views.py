from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.forms.models import model_to_dict
from .models import Article
from .models import CoverPhoto
from .forms import PhotoForm, ArticleForm
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def homepage(request):
	articles = Article.objects.all()
	cover_photos = CoverPhoto.objects.order_by('order').all()
	cover_photos_list = []
	official = []
	if len(cover_photos) > 1:
		cover_photos_list = cover_photos[1:]
		official = cover_photos[0]
	elif len(cover_photos) == 0:
		official = None
	return render(request, 'home/index.html', {'articles': articles, 'cover_photos': cover_photos_list, 'official': official})

@login_required
def edit_photos(request):
	photos = CoverPhoto.objects.all()
	return render(request, 'photos/edit_photos.html', {'photos': photos })

@login_required
def edit_articles(request):
	articles = Article.objects.all()
	return render(request, 'articles/edit_articles.html', {'articles': articles })

class PhotoCreate(CreateView):
	model = CoverPhoto
	form_class = PhotoForm
	template_name = "photos/photo_list.html"
	success_url = reverse_lazy('home:manage_photos')

	def get_context_data(self, **kwargs):
		context = super(PhotoCreate, self).get_context_data(**kwargs)
		photos = CoverPhoto.objects.all()
		context['method'] = 'create'
		context['photos']= photos
		return context

class PhotoUpdate(UpdateView):
	model = CoverPhoto
	form_class = PhotoForm
	template_name = "photos/photo_list.html"
	context_object_name = 'photo'
	success_url = reverse_lazy('dashboard:index')

	def get_context_data(self, **kwargs):
		context = super(PhotoUpdate, self).get_context_data(**kwargs)
		photos = CoverPhoto.objects.all()
		context['method'] = 'update'
		context['photos']= photos
		return context

class PhotoDelete(DeleteView):
	model = Article
	template_name = "music/confirm_delete.html"
	success_url = reverse_lazy('dashboard:index')

class ArticleCreate(CreateView):
	model = Article
	form_class = ArticleForm
	template_name = "articles/manage_articles.html"
	success_url = reverse_lazy('dashboard:index')

	def get_context_data(self, **kwargs):
		context = super(ArticleCreate, self).get_context_data(**kwargs)
		articles = Article.objects.all()
		context['method'] = 'create'
		context['articles'] = articles
		return context

class ArticleUpdate(UpdateView):
	model = Article
	form_class = ArticleForm
	template_name = "articles/manage_articles.html"
	context_object_name = 'article'
	success_url = reverse_lazy('dashboard:index')

	def get_context_data(self, **kwargs):
		context = super(ArticleUpdate, self).get_context_data(**kwargs)
		articles = Article.objects.all()
		context['method'] = 'update'
		context['articles'] = articles
		return context

class ArticleDelete(DeleteView):
	model = Article
	template_name = "music/confirm_delete.html"
	success_url = reverse_lazy('dashboard:index')
