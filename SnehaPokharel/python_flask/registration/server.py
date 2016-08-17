from flask import Flask, render_template, request, redirect, flash, session  
app = Flask(__name__)
app.secret_key = 'Work'

import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NO_NUMBERS = re.compile(r'[a-zA-Z]')

@app.route('/')
def survey():
    return render_template('index.html')


@app.route('/submit', methods = ['POST'])
def results():
	data = request.form

	if request.form['email'] == "":
		flash("You must fill out all the information required!")
	elif request.form['firstname'] == "":
		flash("You must fill out all the information required!")
	elif request.form['lastname'] == "":
		flash("You must fill out all the information required!")
	elif request.form['password'] == "":
		flash("You must fill out all the information required!")
	elif request.form['confirmpassword'] == "":
		flash("You must fill out all the information required!")
	else:
		pass  

	if NO_NUMBERS.match(request.form['firstname']):  
		pass
	elif request.form['firstname'] == "":
		pass 	
	else: 
		flash("First Name should not contain any numbers!")	

	if NO_NUMBERS.match(request.form['lastname']):  
		pass
	elif request.form['firstname'] == "":
		pass 		
	else: 
		flash("Last Name should not contain any numbers!")	

	if len(request.form['password']) < 8: 
		flash("Password should be more than 8 characters")
	else:
		pass 

	if request.form['password'] != request.form['confirmpassword']:
		flash("Passwords should match!")
	else:
		pass

	if EMAIL_REGEX.match(request.form['email']):
		pass 
	else:
		flash("Please enter a valid email address.") 

	print data 
	return render_template('users.html', data=data) 

app.run(debug=True)