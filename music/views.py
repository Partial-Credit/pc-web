from django.shortcuts import render

# Create your views here.
def media(request):
	return render(request, 'music/media.html')