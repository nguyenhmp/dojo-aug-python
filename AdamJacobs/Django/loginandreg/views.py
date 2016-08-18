from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
	user = User.objects.all()
	return render(request, 'loginandreg/index.html')

def success(request):
	return render(request, 'loginandreg/success.html')

def register(request):
	new_user = {
		'first_name':request.POST['first_name'],
		'last_name':request.POST['last_name'],
		'email':request.POST['email'],
		'password':request.POST['password'],
		'confirm_password':request.POST['confirm_password']
	}
	user=User.userManager.register(new_user)
	if user == True:
		me = User.objects.get(email=request.POST['email'])
		request.session['user'] = me.first_name
		return redirect('/loginandreg/success')
	if user[0] == False:
		errors = user[1]
		print user[1]
		for key in user[1]:
			messages.add_message(request, messages.ERROR, user[1][key])
		return redirect('/loginandreg')

def login(request):
	user = {
		'email':request.POST['email'],
		'password':request.POST['password']
	}
	user=User.userManager.login(user)
	if user == True:
		me = User.objects.get(email=request.POST['email'])
		request.session['user'] = me.first_name
		return redirect('/loginandreg/success')
	if user[0] == False:
		messages.add_message(request, messages.ERROR, user[1]['failure'])
		return redirect('/loginandreg')