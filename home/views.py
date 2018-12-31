from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Article
from .models import CoverPhoto

def homepage(request):
	articles = Article.objects.all()
	cover_photos = CoverPhoto.objects.order_by('order').all()
	return render(request, 'home/index.html', {'articles': articles, 'cover_photos': cover_photos[1:], 'official': cover_photos[0]})
