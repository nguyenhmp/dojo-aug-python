from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'sexyorange'
mysql = MySQLConnector(app,'flask_mysql')

@app.route('/')
def index():
	display = mysql.query_db("SELECT * FROM friends")
	print display
 	return render_template('index.html', all_friends=display)

@app.route('/create', methods = ['POST'])
def create():
  		query = "INSERT INTO friends (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())"
  		data = {
  			'first_name': request.form['first_name'],
  			'last_name': request.form['last_name'],
  			'email': request.form['email']
  		}
  		mysql.query_db(query, data)
  		return redirect('/')

@app.route('/friends/<id>/edit')
def editOptions(id):
	query = "SELECT id, first_name, last_name, email, created_at FROM friends WHERE id = :id"
	data = {
	'id' : id
	}
	display = mysql.query_db(query, data)
	print display
 	return render_template('friend.html', friend=display)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
	data = {
	'first_name': request.form['first_name'],
  	'last_name': request.form['last_name'],
  	'email': request.form['email'],
	'id' : id
	}
	mysql.query_db(query, data)
 	return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
	query = "DELETE FROM friends WHERE id = :id"
	data = {'id' : id}
	mysql.query_db(query, data)
 	return redirect('/')

app.run(debug=True)
