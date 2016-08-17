from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	user = User.objects.all()
	return render(request, 'loginandreg/index.html')

def success(request):
	return render(request, 'loginandreg/success.html')

def register(request):
	user=User.userManager.register(request.POST)
	if user == True:
		me = User.objects.get(email=request.POST['email'])
		request.session['user'] = me.first_name
		return redirect(reverse('success'))
	if user[0] == False:
		errors = user[1]
		print user[1]
		for key in user[1]:
			messages.add_message(request, messages.ERROR, user[1][key])
		return redirect(reverse('loginandreg'))

def login(request):
	user = {
		'email':request.POST['email'],
		'password':request.POST['password']
	}
	user=User.userManager.login(user)
	if user == True:
		me = User.objects.get(email=request.POST['email'])
		request.session['user'] = me.id
		return redirect(reverse('success'))
	if user[0] == False:
		messages.add_message(request, messages.ERROR, user[1]['failure'])
		return redirect(reverse('loginandreg'))