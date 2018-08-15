from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.apps import AppConfig
import sys
sys.path.append(sys.path[0] + "\\users")
from users.models import Member

def index(request):
	members = Member.objects.all()
	return render(request, 'about/index.html', {"members": members})
