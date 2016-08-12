from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'disappearing_ninjas/index.html')

def ninjas(request, colors):
	context = {
	'colors' : colors
	}
	return render(request, 'disappearing_ninjas/ninjas.html', context)

