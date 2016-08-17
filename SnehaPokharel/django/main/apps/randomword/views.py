from django.shortcuts import render, HttpResponse, redirect

import uuid


def index(request): #this is where your methods and functions will go. just like in flask, 
#you can return multiple parameters including dictionary which allows you to use django rendering templates to pass vairables. 
	
	if 'counter' in request.session:
		pass 
	else: 
		request.session['counter'] = 1

	random = str(uuid.uuid4()) # Convert UUID format to a Python string.
	random = random.upper() # Make all characters uppercase.
	random = random.replace("-","") # Remove the UUID '-'.
	randomness = random[0:14] # Return the random string.
	context = { "random_number" : randomness}
	return render(request, "randomword/index.html", context)

def increment(request):
	if 'counter' in request.session:
		request.session['counter'] += 1
	else:
		request.session.clear()
	return redirect('/')

def reset(request):
	request.session.clear()
	request.session['counter'] = 0
	return redirect('/')