from __future__ import unicode_literals

from django.db import models
from ..loginandreg.models import User
# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=45)
	author = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	
class Review(models.Model):
	review = models.CharField(max_length=1000)
	rating = models.CharField(max_length=10)
	book = models.ForeignKey(Book, related_name='bookreview')
	user = models.ForeignKey(User, related_name='reviewauthor')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)