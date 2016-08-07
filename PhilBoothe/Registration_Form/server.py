from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = 'testkey'

#regex: check for numbers in name = r'\d'
#regex: check for valid email = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process', methods=['POST'])
def register():
	errorCount = 5
	# store first_name
	session['first_name'] = request.form['first_name']
	print'first_name ' + str(session['first_name'])
	if len(session['first_name']) < 1:
		flash("Please enter your first name.", "First name")
	elif re.search(r'\d', session['first_name']):
		flash ("Names cannot contain numerical characters.", "First name")
	else:
		errorCount -= 1
	# store last_name
	session['last_name'] = request.form['last_name']
	print'last_name ' + str(session['last_name'])
	if len(session['last_name']) < 1:
		flash("Please enter your last name.", "Last name")
	elif re.search(r'\d', session['last_name']):
		flash("Names cannot contain numerical characters.", "Last name")
	else:
		errorCount -= 1
	# store email
	session['email'] = request.form['email']
	print'email ' + str(session['email'])
	if len(session['email']) < 1:
		flash("Please enter your email address.", "Email")
	elif not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', session['email']):
		flash("Please enter a valid email address.", "Email")
	else:
		errorCount -= 1
	# store password
	session['password'] = request.form['password']
	print'password ' + str(session['password'])
	if len(session['password']) < 1:
		flash("Please enter a password.", "Password")
	elif len(session['password']) < 9:
		flash("Password must be more than 8 characters.", "Password")
	elif re.search(r'[A-Z]', session['password'])==False or re.search(r'[0-9]', session['password'])==False:
		flash("Password must contain at least one uppercase letter and one number", "Password")
	else:
		errorCount -= 1
	# store confirm password
	session['conf_password'] = request.form['conf_password']
	print'conf_password ' + str(session['conf_password'])
	if session['conf_password'] != session['password']:
		flash("Your password must match.", "Password")
	else:
		errorCount -= 1
	if errorCount < 1:
		flash("You have successfully registered!", "Valid")
	return redirect('/')

app.run(debug=True)