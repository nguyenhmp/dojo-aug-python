from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'sexyorange'

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME = re.compile(r'.[a-zA-Z]')

name = None
location = None
@app.route('/')
def index():
	if 'success' in session:
		pass
	else:
		session['success'] = 'Please complete the form'
 	return render_template('index.html')

@app.route('/results', methods = ['POST'])
def create_student():
  	session['success'] = 'Thanks for submitting your information.'
  	email = request.form['email']
  	first_name = request.form['first_name']
  	last_name = request.form['last_name']
  	password = request.form['password']
  	confirm_password = request.form['confirm_password']
  	if len(email) < 1:
  		flash('Please provide a valid email address')
  	elif not EMAIL_REGEX.match(request.form['email']):
  		flash('Invalid Email Address!')
  	else:
  		pass
  	if len(first_name) < 1:
  		flash('Please type your first name')
  	elif not NAME.match(request.form['first_name']):
  		flash('Please only use alphabetical characters')
  	else:
  		pass
  	if len(last_name) < 1:
  		flash('Please type your last name')
  	elif not NAME.match(request.form['last_name']):
  		flash('Please only use alphabetical characters')
  	else:
  		pass
  	if len(password) < 8:
  		flash('Password must be at least 8 characters')
  	else:
  		pass
  	if confirm_password != password:
  		flash('Password and confirmation must match')
  	else:
  		pass
  	return redirect('/')

app.run(debug=True)
