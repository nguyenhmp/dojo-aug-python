from django.shortcuts import render, HttpResponse, redirect


def index(request):
	return HttpResponse('No ninjas here!')

def show(request):
	return render(request, "disappearing_ninjas/show_all.html")

def showNinja(request, color):
	context = {'color': str(color)}
	return render(request, "disappearing_ninjas/show.html", context)
