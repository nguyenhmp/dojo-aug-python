from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
# CONTROLLER!!!
# Create your views here.
def index(request):
	return render(request, 'timedisplay/index.html')
