from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from .models import Article
from .models import CoverPhoto
from .forms import PhotoForm

def homepage(request):
	articles = Article.objects.all()
	cover_photos = CoverPhoto.objects.order_by('order').all()
	return render(request, 'home/index.html', {'articles': articles, 'cover_photos': cover_photos[1:], 'official': cover_photos[0]})

def photo_list(request):
	photos = CoverPhoto.objects.all()
	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home:manage_photos')
	else:
		form = PhotoForm()
	return render(request, 'photos/photo_list.html', {'form': form, 'photos': photos})