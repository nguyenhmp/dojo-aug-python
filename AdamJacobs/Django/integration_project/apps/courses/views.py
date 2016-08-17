from django.shortcuts import render, HttpResponse, redirect
from . models import Courses
from ..loginandreg.models import User
from django.core.urlresolvers import reverse
from django.db.models import Count
# CONTROLLER!!!
# Create your views here.
def index(request):
	query = Courses.objects.all()
	context={
	'query':query
	}
	return render(request, 'courses/index.html', context)

def process(request):
	name = request.POST['name']
	description = request.POST['description']
	course = Courses.objects.create(name=name, description=description)
	print course
	return redirect(reverse('courses'))

def frankencourse(request):
	course = Courses.objects.get(id=request.POST['course'])
	user = request.POST['user']
	update = User.objects.get(id=user)
	update.course = course
	update.save() 
	print update.course.id
	return redirect(reverse('user_courses'))

def remove(request, id):
	user = Courses.objects.filter(id=id)
	context={
	'user':user
	}
	return render(request, 'courses/remove.html', context)

def delete(request, id):
	Courses.objects.filter(id=id).delete()
	return redirect(reverse('courses'))

def user_courses(request):
	query = Courses.objects.all().annotate(usercount=Count('usercourse'))
	usercourses = User.objects.all()
	context={
	'query':query,
	'usercourses':usercourses
	}
	return render(request, 'courses/user_courses.html', context)
