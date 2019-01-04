from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

# Create your views here.
def audition(request):
	return  render(request, 'auditions/audition.html')