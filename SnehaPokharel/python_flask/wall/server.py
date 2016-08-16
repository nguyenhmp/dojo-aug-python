from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'omg'

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

import datetime

mysql = MySQLConnector(app,'thewall')

@app.route('/')
def home():
	if 'id' in session:
		session.clear()

	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
	error = False 
	if len(request.form['first_name']) < 2 or str.isalpha(str(request.form['first_name'])) == False:  
		error = True
		flash("Please enter a valid first name!")
	if len(request.form['last_name']) < 2 or str.isalpha(str(request.form['last_name'])) == False:
		error = True
		flash("Please enter a valid last name!")
	if not EMAIL_REGEX.match(request.form['email']):
		error = True
		flash("Please enter a valid email address!")
	if len(request.form['password']) < 8: 
		error = True
		flash("Password must be atleast 8 characters!")
	if request.form['password']!= request.form['cPassword']:
		error = True
		flash("Please enter matching passwords!")
	if error:
		return redirect('/')
	
	else:

		password = request.form['password']
		pw_hash = bcrypt.generate_password_hash(password)

		data = {
		'first_name' : request.form['first_name'],
		'last_name' : request.form['last_name'],
		'email' : request.form['email'],
		'password': pw_hash,
		}

		query= "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"

		session['id'] = mysql.query_db(query, data)
		session['first_name'] = request.form['first_name']
		return redirect('/wall')

@app.route('/login', methods=['POST'])
def login():	
	
	error = False

	if len(request.form['email']) < 1: 
		error = True 
		flash("You forgot to enter your email!")

	if len(request.form['password']) < 1: 
		error = True
		flash("You forgot to enter your password")

	if error:
		return redirect('/')
	else:

		email = request.form['email']
		password = request.form['password']
		query = "SELECT * FROM users WHERE email = :email"
		data = {
			"email": email 
		} 

		user = mysql.query_db(query, data)

		if len(user) == 0:
			flash("No User Found!")
			return redirect('/')

		if bcrypt.check_password_hash(user[0]['password'], password):
			session['first_name'] =  user[0]['first_name'] # we need to store this value to display in wall html first name
			session['id'] = user[0]['id'] #stores the user id that is being logged in
			return redirect('/wall')
		else:
			flash("The email/password does not match. Please try again!")
			return redirect ('/')


@app.route('/wall') #the main route that displays and renders the wall html template. all data in the wall is displayed here. 
def beyondThewall():

	if 'id' in session:
	
		query = "SELECT users.id AS user_id, users.first_name, messages.message, DATE_FORMAT(messages.created_at, '%M %D %Y') AS created_at, users.last_name, messages.id AS message_id FROM users JOIN messages ON users.id = messages.user_id ORDER BY messages.created_at DESC" 
		session['messages'] = mysql.query_db(query) #
		
		query2 = "SELECT users.id AS user_id, users.first_name, comments.message_id, comments.comment, DATE_FORMAT(comments.created_at, '%M %D %Y') AS comments_created_at, users.last_name  FROM users JOIN comments ON users.id = comments.user_id"
		session['comments'] = mysql.query_db(query2)

		#need both of these queries to select all the data for both comments and messages tables and then these values are used to compare in wall HTML. very important to display the correct comment to correct message.
		# print session['comments']

		# print session['messages']

		return render_template('wall.html')	

	else:
		return render_template('index.html') # this prevents anyone from accessing a wall without logging in 	
	
@app.route('/post', methods=['POST']) #this route allows user to post messages and redirects to the wall route. 
def postMessage():
	user_id = session['id']
	data = {'message' : request.form['postinfo'],'user_id' : user_id,}
	query= "INSERT INTO messages(message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :user_id )"

	mysql.query_db(query, data)
	return redirect('/wall')

@app.route('/comment', methods=['POST']) #this route allows you to post comments
def postComment():
	user_id = session['id']
	message_id = request.form['message_id']
	print message_id 
	print "*"*10
	query= "INSERT INTO comments(comment, created_at, updated_at, user_id, message_id) VALUES(:comment, NOW(),NOW(), :user_id, :message_id)"
	data = {'comment' : request.form['comment'],'user_id' : user_id, 'message_id' :message_id}
	print data 

	print mysql.query_db(query, data)
	return redirect('/wall')

app.run(debug=True)