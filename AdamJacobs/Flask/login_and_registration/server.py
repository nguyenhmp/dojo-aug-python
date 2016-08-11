from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = 'sexyorange'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'flask_mysql')

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME = re.compile(r'.[a-zA-Z]')

@app.route('/')
def index():
 	return render_template('index.html')

@app.route('/register', methods = ['POST'])
def create():
	if len(request.form['first_name']) < 2:
  		flash('Please type your first name')
  		return redirect('/')
  	elif not NAME.match(request.form['first_name']):
  		flash('Please only use alphabetical characters')
  		return redirect('/')
  	elif len(request.form['last_name']) < 2:
  		flash('Please type your last name')
  		return redirect('/')
  	elif not NAME.match(request.form['last_name']):
  		flash('Please only use alphabetical characters')
  		return redirect('/')
	elif len(request.form['email']) < 1:
  		flash('Please provide a valid email address')
  		return redirect('/')
  	elif not EMAIL_REGEX.match(request.form['email']):
  		flash('Invalid Email Address!')
  		return redirect('/')
  	elif len(request.form['password']) < 8:
  		flash('Password must be at least 8 characters')
  		return redirect('/')
  	elif request.form['confirm_password'] != request.form['password']:
  		flash('Password and confirmation must match')
  		return redirect('/')
  	else:
  		password = request.form['password']
  		pw_hash = bcrypt.generate_password_hash(password)
  		query = "INSERT INTO registered (first_name, last_name, email, pw_hash, created_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW())"
  		data = {
  			'first_name': request.form['first_name'],
  			'last_name': request.form['last_name'],
  			'email': request.form['email'],
  			'pw_hash': pw_hash
  		}
  		mysql.query_db(query, data)
  		return render_template('success.html')

@app.route('/login', methods = ['POST'])
def login():
  		email = request.form['email']
  		password = request.form['password']
  		user_query = "SELECT email, pw_hash FROM registered WHERE email = :email LIMIT 1"
  		user_data = {'email': email}
  		user = mysql.query_db(user_query, user_data)
  		if bcrypt.check_password_hash(user[0]['pw_hash'], password):
  			return render_template('success.html')
  		else:
  			flash('Incorrect username and password.  Please try again.')
  			return redirect('/')

app.run(debug=True)
