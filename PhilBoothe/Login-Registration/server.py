from flask import Flask, flash, redirect, render_template, request, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
from re import match, search

app = Flask(__name__)
app.secret_key = 'greatestkeyintheworld'
mysql = MySQLConnector(app, 'mydb')
bcrypt = Bcrypt(app)

@app.route('/')
def index():
	# Clear session to remove id
	if 'id' in session:
		session.pop('id')
	return render_template('index.html')

@app.route('/welcome')
def signIn():
	query = "SELECT * FROM users WHERE id=:id"
	data = { 'id': session['id'] }
	user = mysql.query_db(query, data)
	return render_template('welcome.html', user_data=user)

@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	query = "SELECT * FROM users WHERE email=:email LIMIT 1"
	data = { 'email': email }
	user = mysql.query_db(query, data)
	if user:
		if bcrypt.check_password_hash(user[0]['pw_hash'], password):
			session['id'] = user[0]['id']
			print session['id']
			return redirect('/welcome')
		else:
			flash("Invalid Password")
	else:
		flash("Email not found")
	return redirect('/')


@app.route('/register', methods=['POST'])
def register():
	errorCheck = False
	# Validate First Name
	first_name = request.form['first_name']
	if len(first_name) < 2:
		flash("First Name must be at least 2 characters long")
		errorCheck = True
	elif match(r'[^a-zA-Z]', str(first_name)):
		flash("First Name must only contain letters")
		errorCheck = True
	# Validate Last Name
	last_name = request.form['last_name']
	if len(last_name) < 2:
		flash("Last Name must be at least 2 characters long")
		errorCheck = True
	elif search(r'[^a-zA-Z]', str(last_name)):
		flash("Last Name must only contain letters")
		errorCheck = True
	# Validate Email
	email = request.form['email']
	if not match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
		flash("Please enter a valid email")
		errorCheck = True
	# Validate Password
	password = request.form['password']
	if len(password) < 8:
		flash("Password must be at least 8 characters long")
		errorCheck = True
	# Validate Conf_Password
	conf_password = request.form['conf_password']
	if password != conf_password:
		flash("Password does not match")
		errorCheck = True
	# Check if all validation checks passed
	if errorCheck == True:
		return redirect('/')
	else:
		pw_hash = bcrypt.generate_password_hash(password)
		query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW())"
		data = {
				'first_name': first_name,
				'last_name': last_name,
				'email': email,
				'pw_hash': pw_hash
				}
		mysql.query_db(query, data)
		flash("You have successfully registered!")
		return redirect('/')

app.run(debug=True)