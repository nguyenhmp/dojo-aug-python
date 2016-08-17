from django.shortcuts import render, HttpResponse, redirect

import uuid

def index(request): #this is where your methods and functions will go. just like in flask, 
#you can return multiple parameters including dictionary which allows you to use django rendering templates to pass vairables. 
	
	if 'counter' in request.session:
		pass 
	else: 
		request.session['counter'] = 1

	return render(request, "survey/index.html")

def submit(request):
	if 'counter' in request.session:
		request.session['counter'] += 1

	data = {"name" :request.POST['name'], "location" :request.POST['location'], "language" :request.POST['language'], "comment" :request.POST['description']}
	
	return  render(request, "survey/show.html", data)

def reset(request):
	request.session.clear()
	request.session['counter'] = 0
	return redirect('/')
# Create your views here.
