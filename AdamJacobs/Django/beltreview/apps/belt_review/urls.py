from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books$', views.books, name='books'),
    url(r'^books/add$', views.addbook, name='add_book'),
    url(r'^books/create$', views.create, name='create'),
    url(r'^books/create_book_review/(?P<id>\d+)$', views.create_book_review, name='create_book_review'),
    url(r'^books/destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
    url(r'^books/logout$', views.logout, name='logout'),
    url(r'^books/bookpage/(?P<id>\d+)$', views.bookpage, name='bookpage'),
    url(r'^books/userpage/(?P<id>\d+)$', views.userpage, name='userpage'),
]