from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'sexyorange'
mysql = MySQLConnector(app,'email')
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
 	return render_template('index.html')

@app.route('/email', methods = ['POST'])
def create():
  	email = request.form['email']
  	if len(email) < 1:
  		flash('Please provide a valid email address')
  		return redirect('/')
  	elif not EMAIL_REGEX.match(request.form['email']):
  		flash('Invalid Email Address!')
  		return redirect('/')
  	else:
  		session['success'] = 'The email address you entered (' + email + ') is a VALID email address!  Thank You!'
  		query = "INSERT INTO email (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
  		data = {
  		'email': request.form['email']
  		}
  		mysql.query_db(query, data)
  		display = mysql.query_db("SELECT * FROM email")
		print display
  		return render_template('success.html', all_emails=display)

@app.route('/delete/<email_id>', methods=['POST'])
def delete(email_id):
	query = "DELETE FROM email WHERE id = :id"
	data = {'id': email_id}
	mysql.query_db(query, data)
	return redirect('/')

app.run(debug=True)
