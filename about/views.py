from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.apps import AppConfig
import sys
sys.path.append(sys.path[0] + "\\users")
from users.models import Member



def index(request):
	sopranos = list()
	altos = list()
	tenors = list()
	basses = list()
	alumni = list()

	members = Member.objects.all().order_by('last_name')
	for member in members:
		if not member.hidden: # Don't include member objects with the hidden flag set. (Used to hide admin panel user if present)
			if(member.current_member):
				if member.voice_part == 'S':
					sopranos.append(member)
				elif member.voice_part == 'A':
					altos.append(member)
				elif member.voice_part == 'T':
					tenors.append(member)
				elif member.voice_part == "B":
					basses.append(member)
			else:
				alumni.append(member)

	alumni.sort(key=lambda x: x.class_year, reverse=True)
	members_list = [{"Sopranos":sopranos}, {"Altos":altos}, {"Tenors":tenors}, {"Basses":basses}]
	return render(request, 'about/index.html', {"members_list": members_list, "alumni_list": alumni})
