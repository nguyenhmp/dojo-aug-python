from __future__ import unicode_literals

from django.db import models
from ..courses.models import Courses
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME = re.compile(r'^[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
	def register(self, new_user):
		messages={}
		if not NAME.match(new_user['first_name']):
			messages['first_match'] = 'Please enter a valid first name'
		if len(new_user['first_name'])<2:
			messages['first_length'] = 'Please enter your entire first name'
		if not NAME.match(new_user['last_name']):
			messages['last_match'] = 'Please enter a valid last name'
		if len(new_user['last_name'])<2:
			messages['last_name'] = 'Please enter your entire last name'
		if not EMAIL_REGEX.match(new_user['email']):
			messages['last_length'] = 'Please enter a valid email address'
		if len(new_user['password'])<8:
			messages['password_length'] = 'Password must be at least 8 characters'
		if new_user['password'] != new_user['confirm_password']:
			messages['password_match'] = 'Password and confirm password do not match'
		if messages:
			return False, messages
		else:
			password = new_user['password'].encode()
			hashed = bcrypt.hashpw(password, bcrypt.gensalt())
			user = User.objects.create(first_name = new_user['first_name'], last_name = new_user['last_name'], email = new_user['email'], password = hashed)
			return True
	def login(self, user):
		messages = {}
		if User.objects.filter(email=user['email']):
			me=User.objects.get(email=user['email'])
			if bcrypt.hashpw(user['password'].encode(), me.password.encode())== me.password:
				return True
			else:
				messages['failure'] = 'Failed!'
				return False, messages
		else:
			messages['failure'] = 'Failed!'
			return False, messages

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	password = models.CharField(max_length=255)
	course = models.ForeignKey(Courses, related_name='usercourse')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()
	objects = models.Manager()