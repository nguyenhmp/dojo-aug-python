from django.shortcuts import render, HttpResponse
# CONTROLLER!!!
# Create your views here.
def index(request):
	from time import localtime, strftime
	time = strftime("%b, %d %Y %I:%M %p", localtime())
	current_time = {
		'now' : time
	}
	return render(request, 'timedisplay/index.html', current_time)