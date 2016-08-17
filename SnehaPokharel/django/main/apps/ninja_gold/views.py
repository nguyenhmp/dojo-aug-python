from django.shortcuts import render, HttpResponse, redirect

from datetime import datetime
import random 

def index(request):
	if 'gold' in request.session:
		pass 
	else:
		request.session['gold'] = 0

	request.session['date']= datetime.now().strftime('%m/%d/%Y   %I:%M:%S %p') 
	
	if 'list' in request.session: # we need to create a list to add into the activity log. updates every time you add the string variable. 
		pass 
	else:
		request.session['list'] = []
	
	return render(request, "index.html")

def show(request, button):

	context = {'button': button}

	if button == "farm":
		number = random.randrange(10,21) 
		request.session['gold']= request.session['gold'] + number 
		request.session['saying'] = str("Earned ") + str(number) + str(" golds from the farm! ") + str(request.session['date']) #printing to the log
		request.session['list'].append({'text': request.session['saying'], 'color': 'green'}) # you need to create a dictionary for the color value
	elif button == "cave":
		number = random.randrange(5,11)
		request.session['gold']= request.session['gold'] + number 
		request.session['saying'] = str("Earned ") + str(number) + str(" golds from the cave! ") + str(request.session['date'])
		request.session['list'].append({'text': request.session['saying'], 'color': 'green'})
	elif button == "house":
		number = random.randrange(2,6)
		request.session['gold']= request.session['gold'] + number
		request.session['saying'] = str("Earned ") + str(number) + str(" golds from the house! ") + str(request.session['date'])
		request.session['list'].append({'text': request.session['saying'], 'color': 'green'})
	elif button == "casino":
		number = random.randrange(-50,51)
		request.session['gold'] = request.session['gold'] + number
		if number > 0: 
			request.session['saying'] = str("Entered a casino and won ") + str(number) + str(" golds from the casino! ") + str(request.session['date'])
			request.session['list'].append({'text': request.session['saying'], 'color': 'green'})
		else:
			request.session['saying'] = str("Entered a casino and lost ") + str(number*-1) + str(" golds... OUCHY!..") + str(request.session['date'])
			request.session['list'].append({'text': request.session['saying'], 'color': 'red'})
	else:
		pass 

	print request.session['list']	
	return redirect('/') 
	return render(request, "index.html", context)

def reset(request):
		request.session.clear()
		return redirect ('/')
