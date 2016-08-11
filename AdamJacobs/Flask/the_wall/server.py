from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = 'sexyorange'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'thewall')

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME = re.compile(r'.[a-zA-Z]')

@app.route('/')
def index():
 	return render_template('index.html')

@app.route('/thewall')
def displaywall():
	session['messages'] = mysql.query_db("SELECT users.first_name, messages.created_at, messages.message, messages.id as messageid FROM users JOIN messages ON users.id=messages.user_id ORDER BY messages.created_at DESC")
	session['comments'] = mysql.query_db("SELECT users.first_name, comments.message_id as comment_message_id, comments.comment, comments.created_at FROM users JOIN comments ON users.id=comments.user_id ORDER BY comments.created_at ASC")
	return render_template('wall.html')

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
  		query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW())"
  		data = {
  			'first_name': request.form['first_name'],
  			'last_name': request.form['last_name'],
  			'email': request.form['email'],
  			'pw_hash': pw_hash
  		}
  		mysql.query_db(query, data)
  		email = request.form['email']
		query2 = "SELECT first_name, id FROM users WHERE email = :email LIMIT 1"
		data2 = {'email': email}
		session['user'] = mysql.query_db(query2, data2)
		session['messages'] = mysql.query_db("SELECT users.first_name, messages.created_at, messages.message, messages.id as messageid FROM users JOIN messages ON users.id=messages.user_id ORDER BY messages.created_at DESC")
		session['comments'] = mysql.query_db("SELECT users.first_name, comments.message_id as comment_message_id, comments.comment, comments.created_at FROM users JOIN comments ON users.id=comments.user_id ORDER BY comments.created_at ASC")
  		return redirect('/thewall')

@app.route('/login', methods = ['POST'])
def login():
  		email = request.form['email']
	  	password = request.form['password']
	  	if len(email) < 2:
	  		flash('Come on man, at least put in an email or something')
	  		return redirect('/')
	  	else:
		  	user_query = "SELECT email, pw_hash FROM users WHERE email = :email LIMIT 1"
		  	user_data = {'email': email}
		  	user = mysql.query_db(user_query, user_data)
		  	if bcrypt.check_password_hash(user[0]['pw_hash'], password):
		  		email = request.form['email']
				query = "SELECT first_name, id FROM users WHERE email = :email LIMIT 1"
				data = {'email': email}
				session['user'] = mysql.query_db(query, data)
				session['messages'] = mysql.query_db("SELECT users.first_name, messages.created_at, messages.message, messages.id as messageid FROM users JOIN messages ON users.id=messages.user_id ORDER BY messages.created_at DESC")
				session['comments'] = mysql.query_db("SELECT users.first_name, comments.message_id as comment_message_id, comments.comment, comments.created_at FROM users JOIN comments ON users.id=comments.user_id ORDER BY comments.created_at ASC")
		  		return render_template('wall.html')
		  	else:
		  		flash('Incorrect username and password.  Please try again.')
		  		return redirect('/')

@app.route('/logout', methods = ['POST'])
def logout():
	session.clear()
	return redirect('/')

@app.route('/message/<id>', methods = ['POST'])
def message(id):
  		query = "INSERT INTO messages (user_id, message, created_at) VALUES (:id, :message, NOW())"
  		data = {
  		'id': id,
  		'message' : request.form['message']
  		}
  		mysql.query_db(query, data)
  		return redirect('/thewall')

@app.route('/delete_message/<id>', methods = ['POST'])
def delete(id):
  		query2 = "DELETE FROM comments WHERE message_id = :id"
  		data2 = {
  		'id': id,
  		}
  		mysql.query_db(query2, data2)
  		query1 = "DELETE FROM messages WHERE id = :id"
  		data1 = {
  		'id': id,
  		}
  		mysql.query_db(query1, data1)
  		return redirect('/thewall')

@app.route('/comment/<message_id>', methods = ['POST'])
def comment(message_id):
  		query = "INSERT INTO comments (user_id, message_id, comment, created_at) VALUES (:user_id, :message_id, :comment, NOW())"
  		data = {
  		'user_id' : session['user'][0]['id'],
  		'message_id': message_id,
  		'comment' : request.form['comment']
  		}
  		mysql.query_db(query, data)
  		return redirect('/thewall')

app.run(debug=True)
