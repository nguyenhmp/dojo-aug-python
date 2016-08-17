from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app, 'email_list')
app.secret_key='firstattempt'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/success')
def success():
	query = "SELECT * FROM emails"
	emails = mysql.query_db(query)
	return render_template('success.html', email_list=emails)

@app.route('/create', methods=['POST'])
def create():
	if re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', request.form['email']):
		query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
		data = { 'email': request.form['email'] }
		mysql.query_db(query, data)
		flash("Email " + str(request.form['email']) + " was successfully added!  Thank you!")
		return redirect('/success')
	else:
		flash("Please enter a valid email address.")
		return redirect('/')

@app.route('/delete/<email_id>', methods=['POST'])
def delete(email_id):
	query = "DELETE FROM emails WHERE id = :id"
	data = { 'id': email_id }
	mysql.query_db(query, data)
	flash("Email #" + str(email_id) + " has successfully been removed.")
	return redirect('/success')

app.run(debug=True)