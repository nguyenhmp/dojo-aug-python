from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import Book, Review, User
#Count used for aggregate counts - .count also an option when just counting something within one table
from django.db.models import Count
# CONTROLLER!!!
# Create your views here.
def index(request):
	#using loginandreg instead of belt_review allows me to pull in html files from other app
	return render(request, 'loginandreg/index.html')

def books(request):
	user = User.objects.get(id=request.session['user'])
	reviews = Review.objects.all()
	books = Book.objects.all()
	context = {
	'user':user,
	'reviews':reviews,
	'books':books
	}
	return render(request, 'belt_review/books.html', context)

def addbook(request):
	user = User.objects.get(id=request.session['user'])
	reviews = Review.objects.all()
	#using order_by allows just showing authors in select field, not author per book
	authors = Book.objects.order_by('author')
	context = {
	'user':user,
	'reviews':reviews,
	'authors':authors
	}
	return render(request, 'belt_review/add_books.html', context)

def create(request):
	title = request.POST['book_name']
	#checks to see if manual field is blank.  If it is, defaults to selection from prepopulated select
	if request.POST['manual_author']!='':
		author = request.POST['manual_author']
	else:
		author = request.POST['existing_author']
	review = request.POST['review']
	rating = request.POST['rating']
	user = User.objects.get(id=request.session['user'])
	book = Book.objects.create(title=title, author=author)
	#because we are using foreign keys, have to create instances of user and book
	review = Review.objects.create(review=review, rating=rating, user=user, book=book)
	print review
	return redirect(reverse('add_book'))

def create_book_review(request, id):
	review = request.POST['review']
	rating = request.POST['rating']
	user = User.objects.get(id=request.session['user'])
	book = Book.objects.get(id=id)
	review = Review.objects.create(review=review, rating=rating, user=user, book=book)
	print review
	return redirect(reverse('books'))

def destroy(request, id):
	Review.objects.get(id=id).delete()
	return redirect(reverse('books'))

def logout(request):
	request.session.clear()
	return render(request, 'loginandreg/index.html')

def bookpage(request, id):
	book = Book.objects.get(id=id)
	reviews = Review.objects.all()
	user = User.objects.get(id=request.session['user'])
	context={
		'book':book,
		'reviews':reviews,
		'user':user
	}
	return render(request, 'belt_review/bookpage.html', context)

def userpage(request, id):
	user = User.objects.get(id=request.session['user'])
	#reviewcount - counts number of users that have reviewed book.  annotate requires .all.  reviewcount is the name we can use to call it.  Review author is the related-name in the table.
	reviewcount = User.objects.all().annotate(reviewcount=Count('reviewauthor'))
	reviews = Review.objects.all()
	context={
		'user':user,
		'reviews':reviews,
		'reviewcount':reviewcount
	}
	return render(request, 'belt_review/userpage.html', context)
