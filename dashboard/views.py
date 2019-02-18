from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.user.has_perm('users.officer'):
        officer = True
    else:
        officer = False


    return render(request, 'dashboard/index.html', {"officer": officer})
